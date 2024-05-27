 /* Header and Navigation */
header {
  background: #4CAF50;
  color: #fff;
  padding: 10px;
  display: flex;
  justify-content: space-between; /* Aligns items horizontally */
  align-items: center; /* Aligns items vertically */
}

header h1 {
  margin: 0; /* Remove default margin */
}

nav {
  display: flex;
  align-items: center; /* Aligns items vertically */
}

.menu-icon {
  display: none;
}

/* Media Query for Small Screens */
@media screen and (max-width: 768px) {
  header {
    flex-direction: column; /* Stack items vertically */
    text-align: center; /* Align text center */
  }

  nav {
    flex-direction: column; /* Stack items vertically */
    text-align: center; /* Align text center */
    width: 100%;
    position: absolute;
    top: 100%; /* Position below header */
    left: 0;
    background: #4CAF50;
    padding: 10px 0;
    display: none; /* Hide by default */
  }

  nav.active {
    display: flex; /* Show when active */
  }

  nav ul {
    display: flex;
    flex-direction: column;
    margin: 0;
    padding: 0;
  }

  nav ul li {
    margin: 10px 0;
  }

  .menu-icon {
    display: block;
    cursor: pointer;
  }
}
