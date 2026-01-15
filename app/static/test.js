const questions = [
  {
    text: "Как часто ты чувствуешь усталость без явной причины?",
    effects: { fatigue: 2, burnout: 1 }
  },
  {
    text: "Сложно ли тебе сосредоточиться на одной задаче?",
    effects: { fatigue: 2 }
  },
  {
    text: "Бывает ли ощущение внутреннего напряжения без повода?",
    effects: { anxiety: 2 }
  },
  {
    text: "Как часто тебя раздражают мелочи?",
    effects: { irritability: 2 }
  },
  {
    text: "Есть ли ощущение, что ты живёшь «на автомате»?",
    effects: { burnout: 2 }
  },
  {
    text: "Часто ли ты прокручиваешь мысли перед сном?",
    effects: { anxiety: 1, fatigue: 1 }
  }
];

const answers = [
  { label: "Почти никогда", value: 0 },
  { label: "Редко", value: 1 },
  { label: "Иногда", value: 2 },
  { label: "Часто", value: 3 },
  { label: "Почти всегда", value: 4 }
];

let index = 0;

let state = {
  fatigue: 0,
  anxiety: 0,
  irritability: 0,
  burnout: 0
};

const app = document.getElementById("app");
const progress = document.getElementById("progress");

function renderQuestion() {
  progress.style.width = `${(index / questions.length) * 100}%`;

  const q = questions[index];

  app.innerHTML = `
    <div class="question">${q.text}</div>
    <div class="answers">
      ${answers.map(a => `
        <button onclick="answer(${a.value})">${a.label}</button>
      `).join("")}
    </div>
  `;
}

function answer(value) {
  const effects = questions[index].effects;

  for (let key in effects) {
    state[key] += effects[key] * value;
  }

  index++;

  if (index < questions.length) {
    renderQuestion();
  } else {
    showResult();
  }
}

function level(score) {
  if (score < 6) return "низкий";
  if (score < 12) return "средний";
  return "высокий";
}

function showResult() {
  progress.style.width = "100%";

  app.innerHTML = `
    <div class="result">
      <h2>Результат</h2>

      <div class="scale">
        <strong>🧠 Ментальная усталость</strong>
        <span>${level(state.fatigue)}</span>
      </div>

      <div class="scale">
        <strong>😵‍💫 Тревожность</strong>
        <span>${level(state.anxiety)}</span>
      </div>

      <div class="scale">
        <strong>🔥 Раздражительность</strong>
        <span>${level(state.irritability)}</span>
      </div>

      <div class="scale">
        <strong>🪫 Эмоциональное выгорание</strong>
        <span>${level(state.burnout)}</span>
      </div>

      <p style="margin-top:20px; color:#94a3b8;">
        Это не диагноз, а индикатор текущей нагрузки.
        Высокие значения — повод замедлиться и пересмотреть режим.
      </p>
    </div>
  `;
}

renderQuestion();
