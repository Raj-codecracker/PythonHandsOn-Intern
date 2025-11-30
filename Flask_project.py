from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Rituraj Shukla — CV</title>
  <style>
    :root{--accent:#0ea5a4;--muted:#6b7280;font-family:Inter, ui-sans-serif, system-ui, -apple-system, 'Segoe UI', Roboto, 'Helvetica Neue', Arial}
    *{box-sizing:border-box}
    body{font-family:var(--font, Inter), sans-serif;margin:0;background:#f7fafc;color:#0f172a;line-height:1.45}
    .container{max-width:900px;margin:32px auto;background:#fff;border-radius:12px;box-shadow:0 8px 30px rgba(2,6,23,.07);overflow:hidden}
    header{display:flex;gap:20px;padding:28px;border-bottom:1px solid #eef2f7}
    .avatar{flex:0 0 110px;height:110px;border-radius:12px;background:linear-gradient(135deg,var(--accent),#60a5fa);display:flex;align-items:center;justify-content:center;color:#fff;font-weight:700;font-size:28px}
    .head-info{flex:1}
    h1{margin:0;font-size:22px}
    .meta{color:var(--muted);margin-top:6px;font-size:14px}
    .layout{display:grid;grid-template-columns:1fr 320px}
    main{padding:28px}
    aside{background:#fbfdff;border-left:1px solid #eef2f7;padding:28px}
    section{margin-bottom:20px}
    h2{font-size:14px;margin:0 0 10px 0;color:#0f172a}
    p.lead{margin:0;color:var(--muted)}
    .detail-list{list-style:none;padding:0;margin:0}
    .detail-list li{margin:6px 0;color:var(--muted);font-size:14px}
    .edu-item{margin-bottom:12px}
    .skill-badge{display:inline-block;padding:6px 10px;border-radius:999px;border:1px solid #e6eef2;margin:6px 6px 0 0;font-size:13px;background:#fff}
    .project{padding:12px;border-radius:8px;border:1px solid #f1f5f9;margin-bottom:10px}
    .contact a{color:var(--accent);text-decoration:none}
    .print-hide{display:inline-block}
    @media(max-width:880px){.layout{grid-template-columns:1fr}.avatar{display:none}.print-hide{display:none}}
    @media print{body{background:#fff} .container{box-shadow:none;border-radius:0} aside{display:none}}
  </style>
</head>
<body>
  <div class="container" role="document">
    <header>
      <div class="avatar">RS</div>
      <div class="head-info">
        <h1>Rituraj Shukla</h1>
        <div class="meta">B.Tech — CSE • Vivekanand Global University, Jaipur • CGPA: 9.64 • Age: Student</div>
        <p class="lead" style="margin-top:12px">Front-end & Python enthusiast with practical project experience (web UI, Python GUIs, and mental-health platform). Strong academics and solid problem-solving & communication skills. Working on impactful, user-friendly digital solutions.</p>
      </div>
    </header>

    <div class="layout">
      <main>
        <section>
          <h2>Education</h2>
          <div class="edu-item">
            <strong>B.Tech — Computer Science & Engineering</strong>
            <div class="meta">Vivekanand Global University, Jaipur — CGPA: 9.64</div>
            <div class="meta">2024 - 2028</div>
          </div>
          <div class="edu-item">
            <strong>Senior Secondary (XII)</strong>
            <div class="meta">Praxis Vidyapeeth — UP Board (2023) — 72.6%</div>
          </div>
          <div class="edu-item">
            <strong>Secondary (X)</strong>
            <div class="meta">Praxis Vidyapeeth — UP Board (2021) — 93.6%</div>
          </div>
        </section>

        <section>
          <h2>Technical Skills</h2>
          <div>
            <span class="skill-badge">Python</span>
            <span class="skill-badge">HTML & CSS</span>
            <span class="skill-badge">C Programming</span>
            <span class="skill-badge">JavaScript</span>
            <span class="skill-badge">Git</span>
            <span class="skill-badge">GitHub</span>
          </div>
        </section>

        <section>
          <h2>Projects</h2>
          <div class="project">
            <strong>NayaSa — Circular Economy Marketplace</strong>
            <div class="meta">July 2025</div>
            <p style="margin:8px 0 0">Front-end platform to buy, sell, donate or repair goods (HTML, CSS, JavaScript). Responsive UI with dynamic listings to promote reuse and sustainability.</p>
          </div>

          <div class="project">
            <strong>Quiz Game</strong>
            <div class="meta">Oct 2024</div>
            <p style="margin:8px 0 0">GUI-based quiz game built with Python's Tkinter library.</p>
          </div>

          <div class="project">
            <strong>HealHub — Mental Well-being Platform</strong>
            <div class="meta">Dec 2024</div>
            <p style="margin:8px 0 0">Platform addressing stress, anxiety and other conditions to help users manage mental health through accessible technology.</p>
          </div>
        </section>

        <section>
          <h2>Certificates</h2>
          <ul class="detail-list">
            <li>Frontend Development — IBM (Virtual), Jul 2025</li>
          </ul>
        </section>

        <section>
          <h2>Achievements & Activities</h2>
          <ul class="detail-list">
            <li>University projects & hackathon participation</li>
            <li>Hands-on development of responsive UIs and Python GUIs</li>
          </ul>
        </section>
      </main>

      <aside>
        <section class="contact">
          <h2>Contact</h2>
          <ul class="detail-list">
            <li>Email: <a href="mailto:rajshuklal17100@gmail.com">rajshuklal17100@gmail.com</a></li>
            <li>Phone: +91-93776158385</li>
            <li>Location: Basti, Uttar Pradesh, 272002</li>
          </ul>
        </section>

        <section>
          <h2>Professional Skills</h2>
          <ul class="detail-list">
            <li>Communication</li>
            <li>Problem Solving</li>
            <li>Leadership</li>
            <li>Team Building</li>
          </ul>
        </section>

        <section>
          <h2>Profile</h2>
          <p class="meta">B.Tech CSE student with strong academics (CGPA 9.64). Experienced in front-end UI development (HTML/CSS/JS) and Python projects (Tkinter GUIs). Interested in building user-focused digital products and contributing to sustainable, ethical tech.</p>
        </section>

        <section>
          <h2>Languages</h2>
          <ul class="detail-list">
            <li>English — Fluent</li>
            <li>Hindi — Native</li>
          </ul>
        </section>

      </aside>
    </div>
  </div>
</body>
</html>
    """

@app.route("/about")
def about():
    return """
    <h1> About this app </h1>
    <h2> Running with Flask — CV page shows the uploaded resume</h2>
    """

if __name__=='__main__':
    app.run(debug=True)
