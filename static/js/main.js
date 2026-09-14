// Theme toggle and initial setup
(() => {
  let root = document.documentElement,
    toggleBtn = document.querySelector('[data-theme-toggle]'),
    savedTheme = localStorage.getItem('pymaster-theme');

  function setTheme(theme, showToast) {
    root.dataset.theme = theme;
    localStorage.setItem('pymaster-theme', theme);
    toggleBtn.innerHTML = '<i class="fa fa-' + (theme === 'dark' ? 'sun' : 'moon') + '"></i>';

    if (showToast) {
      let toast = document.createElement('div');
      toast.className = 'toast show';
      toast.innerHTML = '<div class="toast-body">' + theme + ' mode enabled</div>';
      document.querySelector('.toast-container')?.append(toast);
      setTimeout(() => toast.remove(), 2000);
    }
  }

  setTheme(savedTheme || 'light');
  if (toggleBtn) {
    toggleBtn.onclick = () => setTheme(root.dataset.theme === 'dark' ? 'light' : 'dark', true);
  }

  const yearEl = document.querySelector('[data-year]');
  if (yearEl) {
    yearEl.textContent = new Date().getFullYear();
  }

  document.querySelectorAll('#nav a').forEach(a => {
    a.onclick = () => bootstrap.Collapse.getInstance(document.querySelector('#nav'))?.hide();
  });

  let observer = new IntersectionObserver(entries => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('is-visible');
        observer.unobserve(entry.target);
      }
    });
  });

  document.querySelectorAll('.reveal').forEach(el => observer.observe(el));
})();

// Quiz answer handler for lesson quizzes using global event delegation
document.addEventListener('click', function(e) {
  const button = e.target.closest('.quiz-answer');
  if (!button) return;

  const parent = button.closest('.quiz-box') || button.closest('.quiz');
  if (!parent) return;

  if (button.disabled || parent.dataset.answered === 'true') return;
  parent.dataset.answered = 'true';

  const selectedOption = (button.dataset.option || button.textContent).trim();
  const correctOption = (button.dataset.correct || parent.dataset.correct || '').trim();
  const explanation = button.dataset.explanation || parent.dataset.explanation || '';
  const feedbackEl = parent.querySelector('.quiz-feedback');
  const allButtons = parent.querySelectorAll('.quiz-answer');

  allButtons.forEach(btn => {
    btn.disabled = true;
    const optText = (btn.dataset.option || btn.textContent).trim();
    if (optText === correctOption) {
      btn.classList.remove('btn-outline-primary', 'btn-primary');
      btn.classList.add('btn-success', 'text-white', 'bg-success', 'border-success');
    }
  });

  if (selectedOption === correctOption) {
    button.classList.remove('btn-outline-primary', 'btn-primary');
    button.classList.add('btn-success', 'text-white', 'bg-success', 'border-success');
    if (feedbackEl) {
      feedbackEl.className = 'quiz-feedback rounded p-3 mt-3 bg-success-subtle text-success border border-success';
      feedbackEl.innerHTML = `<strong>✓ Correct!</strong> ${explanation}`;
      feedbackEl.hidden = false;
    }
  } else {
    button.classList.remove('btn-outline-primary', 'btn-primary');
    button.classList.add('btn-danger', 'text-white', 'bg-danger', 'border-danger');
    if (feedbackEl) {
      feedbackEl.className = 'quiz-feedback rounded p-3 mt-3 bg-danger-subtle text-danger border border-danger';
      feedbackEl.innerHTML = `<strong>✗ Incorrect!</strong> The correct answer is: <strong>${correctOption}</strong>.<br><small class="mt-1 d-block">${explanation}</small>`;
      feedbackEl.hidden = false;
    }
  }
});


// Topic quiz handler
(() => {
  const quiz = document.querySelector('#topicQuiz');
  if (quiz) {
    const result = document.querySelector('#quizResult'),
      retry = document.querySelector('#retryQuiz'),
      quizPage = document.querySelector('.quiz-page'),
      submitBtn = document.querySelector('#submitQuizBtn'),
      key = 'pymaster-quiz-' + (quizPage ? quizPage.dataset.quiz : 'default');

    quiz.addEventListener('submit', event => {
      event.preventDefault();
      const groups = [...quiz.querySelectorAll('fieldset')];

      // Reset previous unanswered warnings
      groups.forEach(g => g.classList.remove('border-danger', 'border-2'));

      // Check if all questions have been answered
      const unanswered = groups.find(g => !g.querySelector(':checked'));
      if (unanswered) {
        unanswered.classList.add('border-danger', 'border-2');
        unanswered.scrollIntoView({ behavior: 'smooth', block: 'center' });

        const feedbackEl = unanswered.querySelector('.question-feedback');
        if (feedbackEl) {
          feedbackEl.className = 'question-feedback rounded-3 p-3 mt-3 bg-danger-subtle text-danger border border-danger fw-semibold';
          feedbackEl.innerHTML = '<strong>⚠️ Please answer this question before submitting!</strong>';
          feedbackEl.hidden = false;
        }
        return;
      }

      let score = 0;

      groups.forEach(g => {
        const chosen = g.querySelector(':checked');
        const correctIdx = Number(chosen.dataset.correct || g.dataset.correct || 0);
        const isCorrect = Number(chosen.value) === correctIdx;
        const labels = [...g.querySelectorAll('.quiz-option-label')];
        const correctLabel = labels[correctIdx];
        const correctText = (chosen.dataset.optionText || (correctLabel ? correctLabel.querySelector('.option-text')?.textContent : '') || '').trim();
        const explanation = (chosen.dataset.explanation || g.dataset.explanation || '').trim();
        const feedbackEl = g.querySelector('.question-feedback');

        // Highlight correct option in green
        if (correctLabel) {
          correctLabel.classList.remove('bg-body-tertiary', 'bg-light');
          correctLabel.classList.add('bg-success-subtle', 'border-success', 'text-success', 'fw-bold');
          
          // Add "✓ Correct Answer" badge if not already added
          if (!correctLabel.querySelector('.correct-badge')) {
            const badge = document.createElement('span');
            badge.className = 'correct-badge ms-auto badge bg-success text-white px-2 py-1 fs-7';
            badge.textContent = '✓ Correct Answer';
            correctLabel.appendChild(badge);
          }
        }

        if (isCorrect) {
          score++;
          if (feedbackEl) {
            feedbackEl.className = 'question-feedback rounded-3 p-3 mt-3 bg-success-subtle text-success border border-success';
            feedbackEl.innerHTML = `<strong>✓ Correct!</strong> ${explanation}`;
            feedbackEl.hidden = false;
          }
        } else {
          // Highlight chosen wrong answer in red
          if (chosen.parentElement) {
            chosen.parentElement.classList.remove('bg-body-tertiary', 'bg-light');
            chosen.parentElement.classList.add('bg-danger-subtle', 'border-danger', 'text-danger');
          }
          if (feedbackEl) {
            feedbackEl.className = 'question-feedback rounded-3 p-3 mt-3 bg-danger-subtle text-danger border border-danger';
            feedbackEl.innerHTML = `<strong>❌ Incorrect!</strong> The correct answer is: <strong>${correctText}</strong>.<br><small class="mt-1 d-block text-body-secondary">${explanation}</small>`;
            feedbackEl.hidden = false;
          }
        }

        // Disable all radio options in this question
        g.querySelectorAll('input').forEach(input => (input.disabled = true));
      });

      const percent = Math.round((score / groups.length) * 100);
      const pass = percent >= 70;

      localStorage.setItem(
        key,
        JSON.stringify({
          score,
          total: groups.length,
          percent,
          pass,
          at: new Date().toISOString()
        })
      );

      // Render top score summary banner
      if (result) {
        if (pass) {
          result.className = 'result-panel card border-0 shadow-sm p-4 mb-4 rounded-3 alert alert-success bg-success-subtle border-success text-success';
          result.innerHTML = `<h3 class="fw-bold mb-1">🎉 Score: ${score} / ${groups.length} (${percent}%)</h3>
          <p class="mb-0 fs-6 fw-semibold text-success-emphasis">Mastery achieved! Excellent understanding of this topic.</p>`;
        } else {
          result.className = 'result-panel card border-0 shadow-sm p-4 mb-4 rounded-3 alert alert-warning bg-warning-subtle border-warning text-warning-emphasis';
          result.innerHTML = `<h3 class="fw-bold mb-1">Score: ${score} / ${groups.length} (${percent}%)</h3>
          <p class="mb-0 fs-6 fw-semibold text-warning-emphasis">Keep practicing! Review the correct answers highlighted in green below and click Retry to try again.</p>`;
        }
        result.hidden = false;
        result.scrollIntoView({ behavior: 'smooth', block: 'center' });
      }

      if (retry) retry.hidden = false;
      if (submitBtn) submitBtn.hidden = true;
    });

    if (retry) {
      retry.onclick = () => location.reload();
    }
  }
})();

// Copy example code handler
const copyExample = document.querySelector('#copyExample');
if (copyExample) {
  copyExample.addEventListener('click', async () => {
    const code = document.querySelector('#exampleSource');
    if (!code) return;
    await navigator.clipboard.writeText(code.textContent);
    const toast = document.createElement('div');
    toast.className = 'toast show';
    toast.innerHTML = '<div class="toast-body">Code copied</div>';
    document.querySelector('.toast-container')?.append(toast);
    setTimeout(() => toast.remove(), 1800);
  });
}

// Example filter input handler
const exampleFilter = document.querySelector('#exampleFilter');
if (exampleFilter) {
  exampleFilter.addEventListener('input', () => {
    const query = exampleFilter.value.trim().toLowerCase();
    document.querySelectorAll('[data-group]').forEach(group => {
      let visibleCount = 0;
      group.querySelectorAll('a').forEach(link => {
        const show = !query || link.dataset.title.includes(query);
        link.hidden = !show;
        if (show) visibleCount++;
      });
      group.hidden = !visibleCount;
    });
  });
}

// Interactive Code Editor / Playground handler
const editor = document.querySelector('#codeEditor');
if (editor) {
  const output = document.querySelector('#playOutput');
  const defaultCode = editor.value;

  document.querySelectorAll('.example-code').forEach(btn => {
    btn.onclick = () => (editor.value = btn.dataset.code);
  });

  const resetBtn = document.querySelector('#resetCode');
  if (resetBtn) {
    resetBtn.onclick = () => {
      editor.value = defaultCode;
      if (output) output.textContent = 'Editor reset.';
    };
  }

  const copyBtn = document.querySelector('#copyCode');
  if (copyBtn) {
    copyBtn.onclick = async () => {
      await navigator.clipboard.writeText(editor.value);
      window.showToast?.('Code copied');
    };
  }

  const clearBtn = document.querySelector('#clearOutput');
  if (clearBtn) {
    clearBtn.onclick = () => {
      if (output) output.textContent = '';
    };
  }

  const runBtn = document.querySelector('#runCode');
  if (runBtn) {
    runBtn.onclick = () => {
      const code = editor.value.trim();
      let outputLines = [];
      const variables = {};

      code.split(/\n/).forEach(line => {
        let strMatch = line.match(/^\s*(\w+)\s*=\s*(["'])(.*?)\2\s*$/);
        if (strMatch) variables[strMatch[1]] = strMatch[3];

        let numMatch = line.match(/^\s*(\w+)\s*=\s*(\d+)\s*$/);
        if (numMatch) variables[numMatch[1]] = numMatch[2];

        let printMatch = line.match(/print\((.*)\)/);
        if (printMatch) {
          let expr = printMatch[1].trim();
          if (/^['"].*['"]$/.test(expr)) {
            outputLines.push(expr.slice(1, -1));
          } else if (variables[expr] !== undefined) {
            outputLines.push(variables[expr]);
          } else if (expr.includes('+')) {
            outputLines.push(
              expr
                .split('+')
                .map(part => {
                  part = part.trim();
                  return variables[part] ?? part.replace(/^['"]|['"]$/g, '');
                })
                .join('')
            );
          } else {
            outputLines.push('[Demo mode: this expression is not supported yet]');
          }
        }
      });

      if (output) {
        output.textContent = outputLines.length
          ? outputLines.join('\n')
          : 'Demo mode supports simple print(), string/integer variables, and selected examples. No code was sent to the server.';
      }
    };
  }
}