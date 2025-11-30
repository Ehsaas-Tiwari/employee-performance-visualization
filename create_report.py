import pandas as pd
import matplotlib.pyplot as plt
import io
import base64

# -------------------------------
# Load the employee dataset
# -------------------------------
data = """employee_id,department,region,performance_score,years_experience,satisfaction_rating
EMP001,IT,Middle East,82.97,4,4.4
EMP002,Operations,Middle East,76.95,6,3.2
EMP003,R&D,Asia Pacific,60.88,10,4.8
EMP004,IT,Middle East,73.7,7,4.3
EMP005,Operations,Europe,79.75,4,4.1
"""

df = pd.read_csv(io.StringIO(data))

# -----------------------------------
# Frequency count for Finance
# -----------------------------------
finance_count = (df["department"] == "Finance").sum()
print("Finance Department Count:", finance_count)

# -----------------------------------
# Create histogram of departments
# -----------------------------------
plt.figure(figsize=(8, 5))
df["department"].value_counts().plot(kind="bar")
plt.title("Department Distribution")
plt.xlabel("Department")
plt.ylabel("Frequency")

# Save the plot into a buffer
buf = io.BytesIO()
plt.savefig(buf, format="png")
buf.seek(0)
encoded_image = base64.b64encode(buf.read()).decode("utf-8")
plt.close()

# -----------------------------------
# Generate HTML report
# -----------------------------------
html = f"""
<html>
<head>
<title>Employee Performance Report</title>
</head>
<body>
<h1>Employee Visualization Report</h1>

<p><b>Email (required for verification):</b> 23f2004056@ds.study.iitm.ac.in</p>

<h2>Finance Department Frequency Count</h2>
<p>{finance_count}</p>

<h2>Department Histogram</h2>
<img src="data:image/png;base64,{encoded_image}" />

</body>
</html>
"""

# Save to HTML file
with open("employee_report.html", "w") as f:
    f.write(html)

print("HTML file generated: employee_report.html")
