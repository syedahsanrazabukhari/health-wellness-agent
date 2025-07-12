# 🧠 Health & Wellness Agent

> **Made by: Syed Ahsan Raza**

A conversational AI assistant that helps users set health goals, get personalized meal and workout plans, track their progress, and escalate to human coaches if needed — all through natural language. The system uses modular agents, functional tools, and a streaming CLI interface to simulate a real-world wellness assistant experience.

---

## 🚀 Features

- Understands natural language health goals like "I want to lose 5kg in 2 months"
- Suggests personalized diet plans and substitutions
- Recommends workouts, including injury-safe options
- Tracks health progress like steps, calories, or activity logs
- Schedules future wellness check-ins
- Escalates to a human coach when the request requires it

---

## 📁 Project Structure

health-wellness-agent/
│
├── custom_agents/ # Specialized agent classes
│ ├── escalation_agent.py # Escalates to human coach
│ ├── injury_support_agent.py # Provides injury-safe workouts
│ └── nutrition_expert_agent.py # Handles dietary requests
│
├── tools/ # Functional tools for planning & tracking
│ ├── goal_analyzer.py
│ ├── meal_planner.py
│ ├── workout_recommender.py
│ ├── scheduler.py
│ └── tracker.py
│
├── utils/
│ └── streaming.py # Output streaming helper
│
├── agent.py # Orchestrator agent factory
├── context.py # Session context model (Pydantic)
├── guardrails.py # Input & output validation
├── hooks.py # Tool and agent lifecycle tracing
├── main.py # CLI entry point
├── .env # Gemini API key config
├── gitignore
├── requirements.txt
└── README.md # You're reading it

## 🛠️ Getting Started

```bash
1. Clone the Repository
git clone https://github.com/yourusername/health-wellness-agent.git
cd health-wellness-agent

2. Install Dependencies
Use pip:
- uv pip install -r requirements.txt

3. Create .env File
Create a .env file in the project root and add your Gemini API key:

GEMINI_API_KEY=your_gemini_api_key_here

4. Run the Agent
python filename.extension

💬 Usage
Once running, the CLI will prompt:

🟢 Type your question (or 'exit' to quit)
Enter any natural language health-related prompt.

✅ Example Prompts
I want to lose 5kg in 2 months

Help me gain muscle

Suggest a balanced vegetarian meal plan

I walked 8000 steps today, track it

Book my check-in for Sunday

Recommend an upper body workout

I have a knee injury, what workout should I do?

Connect me to a human coach

hello

hi

```

## 🧠 Agents

### Agent Name Description

- HealthWellnessAgent The main orchestrator agent
- NutritionExpertAgent Recommends diet plans and substitutions
- InjurySupportAgent Suggests safe workouts considering injuries
- EscalationAgent Escalates conversation to a human coach

## 🧰 Tools

### Tool Name Function

- goal_analyzer Reformulates goal in a motivating way.
- meal_planner Suggests high-level diet advice.
- workout_recommender Recommends simple routines based on goal.
- progress_tracker Logs progress with encouragement.
- checkin_scheduler Schedules weekly or daily health check-ins.

## 🛡️ Input Validation

The app uses smart filtering to allow natural prompts while blocking clearly inappropriate or irrelevant messages.

### ✅ Accepts

- "I want to lose 5kg"

- "hello", "hi"

- "track my progress"

- "schedule a workout"

### ❌ Rejects

- Empty strings

- Profanity or abusive language

- Nonsense like "asdjlk"

## 🧱 Tech Stack

- Python 3.10+

- AsyncOpenAI (Gemini-compatible)

- Pydantic

- Streaming CLI Interface

- Modular tool & agent architecture

## 🌱 Future Improvements

- Persistent storage for user history

- Google Calendar integration for scheduling

- Streamlit or web-based front-end

- NLP-based goal parsing

- Advanced nutrition macros and calorie tracking

## 👨‍💻 Author

- Syed Ahsan Raza

- Frontend Developer | Python Enthusiast

- 📍 Karachi, Pakistan

- 🌐 GitHub: github.com/yourusername

- 🔗 LinkedIn: linkedin.com/in/yourname

## 📜 License

This project is provided for personal, academic, or demo use. For commercial licensing or collaboration, please contact the author.
