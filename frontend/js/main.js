document.addEventListener('DOMContentLoaded', () => {
    loadPortfolio();
    loadSkills();
    loadProjects();
  
    // Event listener for toggling mobile navigation
    document.querySelector('.main_nav_burger').addEventListener('click', function() {
      document.querySelector('.mobile_nav').classList.toggle('active');
    });
  });
  
  const API = {
    portfolio: {
        get: '/api/portfolio',
    },
    skills: {
        get: '/api/skills',
    },
    projects: {
        get: '/api/projects',
    }
  };
  
  function loadPortfolio() {
    fetch(API.portfolio.get)
        .then(response => response.json())
        .then(data => {
            const portfolioContent = document.getElementById('portfolio-content');
            portfolioContent.innerHTML = data.map(item => `
                <div class="portfolio-item" onclick="openModal('${item.title}', '${item.description}')">
                    <h3>${item.title}</h3>
                    <p>${item.description}</p>
                </div>
            `).join('');
        })
        .catch(error => console.error('Error loading portfolio:', error));
  }
  
  function loadSkills() {
    fetch(API.skills.get)
        .then(response => response.json())
        .then(data => {
            const skillsList = document.getElementById('skills-list');
            skillsList.innerHTML = data.map(skill => `<div class="skill">${skill.skill_name}</div>`).join('');
        })
        .catch(error => console.error('Error loading skills:', error));
  }
  
  function loadProjects() {
    fetch(API.projects.get)
        .then(response => response.json())
        .then(data => {
            const projectsContent = document.getElementById('projects-content');
            projectsContent.innerHTML = data.map(project => `
                <div class="project" data-category="${project.category}">
                    <h3>${project.project_name}</h3>
                    <p>${project.project_description}</p>
                </div>
            `).join('');
        })
        .catch(error => console.error('Error loading projects:', error));
  }
  
  function addSkill() {
    const newSkillInput = document.getElementById('new-skill');
    const newSkill = newSkillInput.value.trim();
    if (newSkill !== '') {
        const skillsList = document.getElementById('skills-list');
        const skillElement = document.createElement('div');
        skillElement.classList.add('skill');
        skillElement.textContent = newSkill;
        skillsList.appendChild(skillElement);
        newSkillInput.value = ''; // Clear input field
    }
  }
  
  function filterProjects(category) {
    const projects = document.querySelectorAll('.project');
    projects.forEach(project => {
        if (category === 'all' || project.dataset.category === category) {
            project.style.display = 'block';
        } else {
            project.style.display = 'none';
        }
    });
  }
  
  function openModal(title, description) {
    const modal = document.getElementById('portfolio-modal');
    const detailsContainer = document.getElementById('portfolio-details');
    detailsContainer.innerHTML = `
        <h3>${title}</h3>
        <p>${description}</p>
    `;
    modal.style.display = 'block';
  }
  
  function closeModal() {
    const modal = document.getElementById('portfolio-modal');
    modal.style.display = 'none';
  }
  
  document.addEventListener('click', function(event) {
    if (event.target.classList.contains('close')) {
        closeModal();
    }
  });
  
  window.addEventListener('click', function(event) {
    const modal = document.getElementById('portfolio-modal');
    if (event.target === modal) {
        closeModal();
    }
  });
  