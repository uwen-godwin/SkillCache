document.addEventListener('DOMContentLoaded', () => {
  const form = document.getElementById("form");
  const email = document.getElementById("email");
  const lastName = document.getElementById("lastname");
  const firstName = document.getElementById("firstname");
  const telephone = document.getElementById("tel");
  const password = document.getElementById("password");
  const password2 = document.getElementById("password2");

  form.addEventListener("submit", (e) => {
      e.preventDefault();
      checkInput();
  });

  function checkInput() {
      // Get the values from the inputs
      const firstNameValue = firstName.value.trim();
      const lastNameValue = lastName.value.trim();
      const emailValue = email.value.trim();
      const telephoneValue = telephone.value.trim();
      const passwordValue = password.value.trim();
      const password2Value = password2.value.trim();

      const strongChecker = new RegExp("(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[^A-Za-z0-9])(?=.{8,})");
      const mediumChecker = new RegExp("((?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[^A-Za-z0-9])(?=.{6,}))|((?=.*[a-z])(?=.*[A-Z])(?=.*[^A-Za-z0-9])(?=.{8,}))");

      if (firstNameValue === "") {
          setErrorFor(firstName, "First name cannot be blank");
      } else {
          setSuccessFor(firstName);
      }

      if (lastNameValue === "") {
          setErrorFor(lastName, "Last name cannot be blank");
      } else {
          setSuccessFor(lastName);
      }

      if (emailValue === "") {
          setErrorFor(email, "Email cannot be blank");
      } else if (!isEmail(emailValue)) {
          setErrorFor(email, "Email is not valid");
      } else {
          setSuccessFor(email);
      }

      if (telephoneValue === "") {
          setErrorFor(telephone, "Please enter a telephone number");
      } else {
          setSuccessFor(telephone);
      }

      if (passwordValue === "") {
          setErrorFor(password, "Password cannot be empty");
      } else if (strongChecker.test(passwordValue)) {
          setSuccessFor(password);
      } else if (mediumChecker.test(passwordValue)) {
          setMediumFor(password, "Password not strong enough");
      } else {
          setErrorFor(password, "Password too weak");
      }

      if (password2Value === "") {
          setErrorFor(password2, "Please confirm your password");
      } else if (passwordValue !== password2Value) {
          setErrorFor(password2, "Passwords do not match");
      } else {
          setSuccessFor(password2);
      }
  }

  function setErrorFor(input, message) {
      const formControl = input.parentElement; // .form-control
      const small = formControl.querySelector("small");
      small.innerText = message; // Add error message inside small
      formControl.className = "form-control error"; // Add error class
  }

  function setMediumFor(input, message) {
      const formControl = input.parentElement; // .form-control
      const small = formControl.querySelector("small");
      small.innerText = message; // Add medium message inside small
      formControl.className = "form-control medium"; // Add medium class
  }

  function setSuccessFor(input) {
      const formControl = input.parentElement;
      const small = formControl.querySelector("small");
      small.innerText = ''; // Clear any previous messages
      formControl.className = "form-control success"; // Add success class
  }

  function isEmail(email) {
      // Regex for email validation
      return /^((([a-z]|\d|[!#$%&'*+/=?^_`{|}~]|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])+(\.([a-z]|\d|[!#$%&'*+/=?^_`{|}~]|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])+)*)|((\x22)((((\x20|\x09)*(\x0d\x0a))?(\x20|\x09)+)?(([\x01-\x08\x0b\x0c\x0e-\x1f\x7f]|\x21|[\x23-\x5b]|[\x5d-\x7e]|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])|(\\([\x01-\x09\x0b\x0c\x0d-\x7f]|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF]))))*(((\x20|\x09)*(\x0d\x0a))?(\x20|\x09)+)?(\x22)))@((([a-z]|\d|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])|(([a-z]|\d|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])([a-z]|\d|-|\.|_|~|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])*([a-z]|\d|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])))\.)+(([a-z]|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])|(([a-z]|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])([a-z]|\d|-|\.|_|~|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])*([a-z]|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])))$/i.test(email);
  }
});

