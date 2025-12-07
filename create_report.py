import pandas as pd
import matplotlib.pyplot as plt
import io
import base64
import textwrap

# ================================
# EMAIL FOR VERIFICATION
# 23f2004056@ds.study.iitm.ac.in
# ================================

python_code_text = """
import pandas as pd
import matplotlib.pyplot as plt
import io
import base64

data = \"\"\"employee_id,department,region,performance_score,years_experience,satisfaction_rating
EMP001,IT,Middle East,82.97,4,4.4
EMP002,Operations,Middle East,76.95,6,3.2
EMP003,R&D,Asia Pacific,60.88,10,4.8
EMP004,IT,Middle East,73.7,7,4.3
EMP005,Operations,Europe,79.75,4,4.1
\"\"\"

df = pd.read_csv(io.StringIO(data))
finance_count = (df["department"] == "Finance").sum()
print("Finance Department Count:", finance_count)

plt.figure(figsize=(6, 4))
df["department"].value_counts().plot(kind="bar")
plt.title("Department Distribution")
plt.xlabel("Department")
plt.ylabel("Frequency")
plt.savefig("chart.png")
plt.close()
"""

# ----------------------------
# Load the employee dataset
# ----------------------------
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
plt.figure(figsize=(6, 4))
df["department"].value_counts().plot(kind="bar")
plt.title("Department Distribution")
plt.xlabel("Department")
plt.ylabel("Frequency")

# Save image to memory
buf = io.BytesIO()
plt.savefig(buf, format="png")
buf.seek(0)
encoded_img = base64.b64encode(buf.read()).decode("utf-8")
plt.close()

# -----------------------------------
# Generate HTML OUTPUT WITH PYTHON CODE EMBEDDED ✅
# -----------------------------------
html_content = f"""
<html>
<head>
<title>Employee Performance Analysis</title>
</head>
<body>

<h1>Employee Department Analysis</h1>
<p><b>Email:</b> 23f2004056@ds.study.iitm.ac.in</p>

<h2>Finance Department Frequency</h2>
<p>{finance_count}</p>

<h2>Department Distribution Histogram</h2>
<img src="data:image/png;base64,{encoded_img}" />

<h2>Python Code Used for Analysis</h2>
<pre><code>
{python_code_text}
</code></pre>

</body>
</html>
"""

with open("employee_report.html", "w") as f:
    f.write(html_content)

print("✅ employee_report.html created with embedded Python code!")
