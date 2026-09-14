(() => {
  const sidebar = document.getElementById("practiceSidebar");
  const shell = document.querySelector(".practice-shell");
  if (!shell) return;

  const KEY = "pymaster-practice-sidebar-scroll";
  const saveScroll = () => {
    if (sidebar) sessionStorage.setItem(KEY, String(sidebar.scrollTop));
  };
  const restoreScroll = () => {
    const y = sessionStorage.getItem(KEY);
    if (sidebar && y != null) sidebar.scrollTop = Number(y);
  };
  if (sidebar) sidebar.addEventListener("scroll", saveScroll, { passive: true });
  restoreScroll();

  let pyodideInstance = null;
  let pyodideLoadingPromise = null;

  const getPyodide = async (output) => {
    if (pyodideInstance) return pyodideInstance;
    if (typeof loadPyodide === "undefined") return null;

    if (!pyodideLoadingPromise) {
      if (output) output.textContent = "Loading Python environment in browser...";
      pyodideLoadingPromise = loadPyodide({
        indexURL: "https://cdn.jsdelivr.net/pyodide/v0.26.4/full/",
      })
        .then((py) => {
          pyodideInstance = py;
          return py;
        })
        .catch((err) => {
          console.warn("Pyodide CDN load failed, using fallback executor:", err);
          pyodideLoadingPromise = null;
          return null;
        });
    }
    return pyodideLoadingPromise;
  };

  const payload = () => {
    const el = document.getElementById("practicePayload");
    if (!el) return { starter: "", tests: "", helper: "" };
    try {
      return JSON.parse(el.textContent);
    } catch (e) {
      return { starter: "", tests: "", helper: "" };
    }
  };

  const bindEditor = () => {
    const editor = document.getElementById("practiceEditor");
    const output = document.getElementById("practiceOutput");
    const resetBtn = document.getElementById("resetPractice");
    const runBtn = document.getElementById("runPractice");
    const checkBtn = document.getElementById("checkPractice");

    if (!editor || !output) return;
    const data = payload();

    if (resetBtn) {
      resetBtn.onclick = () => {
        editor.value = data.starter;
        output.textContent = "Editor reset to starter code.";
        output.classList.remove("ok", "bad");
      };
    }

    const runFallback = (withTests) => {
      const userCode = editor.value.trim();
      let printedLines = [];
      let vars = {};

      userCode.split(/\n/).forEach((line) => {
        let strM = line.match(/^\s*(\w+)\s*=\s*(["'])(.*?)\2\s*$/);
        if (strM) vars[strM[1]] = strM[3];

        let numM = line.match(/^\s*(\w+)\s*=\s*(-?\d+)\s*$/);
        if (numM) vars[numM[1]] = Number(numM[2]);

        let printM = line.match(/print\((.*)\)/);
        if (printM) {
          let expr = printM[1].trim();
          if (/^['"].*['"]$/.test(expr)) {
            printedLines.push(expr.slice(1, -1));
          } else if (vars[expr] !== undefined) {
            printedLines.push(String(vars[expr]));
          } else if (expr.includes("+")) {
            let parts = expr.split("+").map((p) => {
              p = p.trim();
              return vars[p] ?? p.replace(/^['"]|['"]$/g, "");
            });
            printedLines.push(parts.join(""));
          } else {
            printedLines.push(expr);
          }
        }
      });

      const userOutput = printedLines.join("\n").trim();

      if (!withTests) {
        output.textContent = userOutput || "Program finished with no printed output.";
        output.classList.remove("ok", "bad");
      } else {
        let expectedMatch = data.tests ? data.tests.match(/_check_output\((["'])(.*?)\1\)/s) : null;
        if (expectedMatch) {
          let expected = expectedMatch[2].replace(/\\n/g, "\n").trim();
          if (userOutput === expected) {
            output.textContent = "✓ Correct! Output:\n" + userOutput;
            output.classList.add("ok");
            output.classList.remove("bad");
          } else {
            output.textContent = `FAIL output:\n got: ${JSON.stringify(userOutput)}\n expected: ${JSON.stringify(expected)}`;
            output.classList.add("bad");
            output.classList.remove("ok");
          }
        } else {
          output.textContent = userOutput || "Code executed.";
          output.classList.remove("ok", "bad");
        }
      }
    };

    const runUser = async (withTests) => {
      output.textContent = "Running...";
      output.classList.remove("ok", "bad");

      let py = null;
      try {
        py = await getPyodide(output);
      } catch (err) {
        console.warn("Pyodide error:", err);
      }

      if (!py) {
        runFallback(withTests);
        return;
      }

      let captured = "";
      try {
        py.setStdout({
          batched: (text) => {
            captured += text + "\n";
          },
        });
        py.setStderr({
          batched: (text) => {
            captured += text + "\n";
          },
        });
      } catch (e) {
        console.warn("setStdout error:", e);
      }

      const userCode = editor.value;

      if (!withTests) {
        const script = [
          "import io, sys",
          "_buf = io.StringIO()",
          "_real = sys.stdout",
          "sys.stdout = _buf",
          "try:",
          "    exec(USER_CODE, globals())",
          "finally:",
          "    sys.stdout = _real",
          "_USER_OUTPUT = _buf.getvalue()",
          "print(_USER_OUTPUT, end='')",
        ].join("\n");

        try {
          py.globals.set("USER_CODE", userCode);
          await py.runPythonAsync(script);
          output.textContent = captured.trim() || "Program finished with no printed output.";
          output.classList.remove("ok", "bad");
        } catch (error) {
          output.classList.add("bad");
          output.classList.remove("ok");
          output.textContent = String(error.message || error);
        }
      } else {
        const script = [
          "import io, sys",
          "_buf = io.StringIO()",
          "_real = sys.stdout",
          "sys.stdout = _buf",
          "try:",
          "    exec(USER_CODE, globals())",
          "finally:",
          "    sys.stdout = _real",
          "_USER_OUTPUT = _buf.getvalue()",
          data.helper || "",
          data.tests || "",
        ].join("\n");

        try {
          py.globals.set("USER_CODE", userCode);
          await py.runPythonAsync(script);

          const trimmed = captured.trim();
          if (trimmed.includes("PASS")) {
            const cleanOutput = trimmed.replace(/PASS/g, "").trim();
            output.textContent = "✓ Correct! All checks passed.\n\n" + (cleanOutput || "Output matched expected result.");
            output.classList.add("ok");
            output.classList.remove("bad");
          } else if (trimmed.includes("FAIL")) {
            output.textContent = trimmed;
            output.classList.add("bad");
            output.classList.remove("ok");
          } else {
            output.textContent = trimmed || "Completed check.";
            output.classList.remove("ok", "bad");
          }
        } catch (error) {
          output.classList.add("bad");
          output.classList.remove("ok");
          output.textContent = String(error.message || error);
        }
      }
    };

    if (runBtn) {
      runBtn.onclick = () => runUser(false);
    }
    if (checkBtn) {
      checkBtn.onclick = () => runUser(true);
    }
  };

  const filterBox = document.getElementById("practiceFilter");
  if (filterBox) {
    filterBox.addEventListener("input", () => {
      const q = filterBox.value.trim().toLowerCase();
      document.querySelectorAll("[data-group]").forEach((group) => {
        let visible = 0;
        group.querySelectorAll("a").forEach((link) => {
          const show = !q || link.dataset.title.includes(q);
          link.hidden = !show;
          if (show) visible += 1;
        });
        group.hidden = !visible;
      });
    });
  }

  const markCurrent = (url) => {
    if (!sidebar) return;
    const path = new URL(url, location.origin).pathname;
    sidebar.querySelectorAll("a[href]").forEach((link) => {
      link.classList.toggle("current", new URL(link.href, location.origin).pathname === path);
    });
  };

  const openProblem = async (url, push) => {
    saveScroll();
    const response = await fetch(url);
    if (!response.ok) {
      location.href = url;
      return;
    }
    const doc = new DOMParser().parseFromString(await response.text(), "text/html");
    const nextMain = doc.querySelector(".practice-main");
    const currentMain = document.querySelector(".practice-main");
    const nextPayload = doc.getElementById("practicePayload");
    const currentPayload = document.getElementById("practicePayload");
    if (!nextMain || !currentMain || !nextPayload || !currentPayload) {
      location.href = url;
      return;
    }
    currentMain.replaceWith(nextMain);
    currentPayload.replaceWith(nextPayload);
    document.title = doc.title;
    markCurrent(url);
    restoreScroll();
    if (push) history.pushState({ practice: true }, "", url);
    bindEditor();
  };

  shell.addEventListener("click", (event) => {
    const link = event.target.closest("a[href]");
    if (!link) return;
    const path = new URL(link.href, location.origin).pathname;
    if (!path.startsWith("/practice/")) return;
    event.preventDefault();
    openProblem(link.href, true);
  });

  window.addEventListener("popstate", () => {
    if (location.pathname.startsWith("/practice/")) openProblem(location.href, false);
  });

  bindEditor();
})();
