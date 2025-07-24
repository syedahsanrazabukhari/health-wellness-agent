from fpdf import FPDF
from datetime import datetime

class WellnessPDFReport:
    def __init__(self, context: dict):
        self.context = context

    def create_pdf(self, filename="wellness_report.pdf"):
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", "B", 16)
        pdf.cell(0, 10, "Health & Wellness Report", ln=True, align="C")

        pdf.set_font("Arial", size=12)
        pdf.ln(10)
        pdf.cell(0, 10, f"User: {self.context.get('name', 'Unknown')}", ln=True)
        pdf.cell(0, 10, f"User ID: {self.context.get('uid', 'N/A')}", ln=True)
        pdf.cell(0, 10, f"Report Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}", ln=True)
        pdf.ln(5)

        pdf.set_font("Arial", "B", 14)
        pdf.cell(0, 10, "🎯 User Goal", ln=True)
        pdf.set_font("Arial", size=12)
        pdf.multi_cell(0, 10, str(self.context.get("goal", "Not provided")))

        pdf.set_font("Arial", "B", 14)
        pdf.cell(0, 10, "🥗 Weekly Meal Plan", ln=True)
        pdf.set_font("Arial", size=12)
        meal_plan = self.context.get("meal_plan", [])
        if meal_plan and isinstance(meal_plan, list):
            for i, meal in enumerate(meal_plan, 1):
                pdf.cell(0, 10, f"Day {i}: {meal}", ln=True)
        else:
            pdf.cell(0, 10, "No meal plan available.", ln=True)

        pdf.set_font("Arial", "B", 14)
        pdf.cell(0, 10, "💪 Workout Schedule", ln=True)
        pdf.set_font("Arial", size=12)
        workout_plan = self.context.get("workout_plan", {})
        if workout_plan:
            pdf.multi_cell(0, 10, str(workout_plan))
        else:
            pdf.cell(0, 10, "No workout plan available.", ln=True)

        try:
            pdf.output(filename)
            print(f"[Report] PDF generated at {filename}")
        except PermissionError:
            print("[Report] Cannot write PDF file. Please close it if open and try again.")
