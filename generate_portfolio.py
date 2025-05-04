import json
from datetime import UTC, datetime
from pathlib import Path

from jinja2 import Environment, FileSystemLoader

# Load JSON data - this should be the path to your JSON file by default portfolio.json
with Path("portfolio.json").open(encoding="utf-8") as f:
    data = json.load(f)

# Add any extra context if needed
data["current_year"] = datetime.now(tz=UTC).year

if "social_links" in data:
    for link in data["social_links"]:
        if link.get("svg_path"):
            with Path(link["svg_path"]).open(encoding="utf-8") as svg_file:
                link["svg_data"] = svg_file.read()

# Set up Jinja environment
env = Environment(loader=FileSystemLoader("."), autoescape=True)
# Load the CV template - this should be the path to your HTML file by default CV_template.html
index_template = env.get_template("FullCV.html")
# Load the resume template - this should be the path to your HTML file by default resume_template.html
resume_template = env.get_template("resumeCV.html")

# Render the template with the data
html_output = index_template.render(**data)
resume_output = resume_template.render(**data)

# This is equivalent to...
# html_output = index_template.render(name=data["name"], label=data["label"]...)
# resume_output = resume_template.render(name=data["name"], label=data["label"]...)

# Write the output to an HTML file
# write the file established for your cv - this is the path to your HTML file by default index.html
with Path("index.html").open("w", encoding="utf-8") as f:
    f.write(html_output)

# write the file established for your resume - this is the path to your HTML file by default resume.html
with Path("resume.html").open("w", encoding="utf-8") as f:
    f.write(resume_output)

print("HTML file generated successfully!")
