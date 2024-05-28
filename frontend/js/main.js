document.addEventListener("DOMContentLoaded", function() {
  loadPortfolio();
  loadSkills();
  loadProjects();
});

function loadPortfolio() {
  fetch('/api/portfolio')
      .then(response => response.json())
      .then(data => {
          const portfolioSection = document.getElementById('portfolio');
          portfolioSection.innerHTML = `<h2>${data.title}</h2><p>${data.description}</p>`;
      })
      .catch(error => console.error('Error:', error));
}

function loadSkills() {
  fetch('/api/skills')
      .then(response => response.json())
      .then(data => {
          const skillsSection = document.getElementById('skills');
          skillsSection.innerHTML = data.skills.map(skill => `<p>${skill.skill_name}</p>`).join('');
      })
      .catch(error => console.error('Error:', error));
}

function loadProjects() {
  fetch('/api/projects')
      .then(response => response.json())
      .then(data => {
          const projectsSection = document.getElementById('projects');
          projectsSection.innerHTML = data.projects.map(project => `<h3>${project.project_name}</h3><p>${project.project_description}</p>`).join('');
      })
      .catch(error => console.error('Error:', error));
}
