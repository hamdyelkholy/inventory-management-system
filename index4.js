document.addEventListener('DOMContentLoaded', () => {
  // Task 1
  const bioInput = document.getElementById('bioInput');
  const charCounter = document.getElementById('charCounter');
  const bioPreview = document.getElementById('bioPreview');

  bioInput.addEventListener('input', () => {
    const remaining = 200 - bioInput.value.length;
    charCounter.textContent = `${remaining} characters remaining`;
    bioPreview.textContent = bioInput.value;
    charCounter.style.color = remaining < 20 ? 'red' : 'black';
  });

  // Task 2
  const mainImage = document.getElementById('mainImage');
  const thumbs = document.querySelectorAll('.thumb');

  thumbs.forEach(btn => {
    btn.addEventListener('click', () => {
      mainImage.setAttribute('src', btn.getAttribute('data-src'));
      mainImage.setAttribute('alt', btn.getAttribute('data-alt'));
      thumbs.forEach(b => b.classList.remove('active'));
      btn.classList.add('active');
    });
  });

  // Task 3
  const itemForm = document.getElementById('itemForm');
  const inventoryContainer = document.getElementById('inventoryContainer');
  const clearInventory = document.getElementById('clearInventory');

  itemForm.addEventListener('submit', (e) => {
    e.preventDefault();
    const name = document.getElementById('itemName').value;
    const price = document.getElementById('itemPrice').value;

    const div = document.createElement('div');
    div.className = 'item-card';
    div.textContent = `Item: ${name} - Price: $${price}`;
    inventoryContainer.appendChild(div);

    itemForm.reset();
  });

  clearInventory.addEventListener('click', () => {
    inventoryContainer.replaceChildren();
  });

  // Task 4
  const faqTitles = document.querySelectorAll('.faq-title');
  faqTitles.forEach(title => {
    title.addEventListener('click', () => {
      const content = title.nextElementSibling;
      content.classList.toggle('hidden');
    });
  });

  // Task 5
  const teamForm = document.getElementById('teamForm');
  const teamList = document.getElementById('teamList');

  teamForm.addEventListener('submit', (e) => {
    e.preventDefault();
    const name = document.getElementById('memberName').value;
    const title = document.getElementById('memberTitle').value;

    const li = document.createElement('li');
    li.innerHTML = `${name} (${title}) <button class="promote-btn">Promote</button> <button class="remove-btn">Remove</button>`;
    teamList.appendChild(li);

    teamForm.reset();
  });

  teamList.addEventListener('click', (e) => {
    if (e.target.classList.contains('remove-btn')) {
      e.target.parentElement.remove();
    } else if (e.target.classList.contains('promote-btn')) {
      e.target.parentElement.classList.toggle('promoted');
    }
  });

  // Task 6
  const themeBtn = document.getElementById('themeBtn');
  themeBtn.addEventListener('click', () => {
    document.body.classList.toggle('dark-mode');
    const isDark = document.body.classList.contains('dark-mode');
    themeBtn.textContent = isDark ? 'Switch to Light Mode' : 'Switch to Dark Mode';
  });

  // Task 7
  const searchInput = document.getElementById('searchInput');
  const skills = document.querySelectorAll('#skillsList li');

  searchInput.addEventListener('input', () => {
    const query = searchInput.value.toLowerCase();
    skills.forEach(skill => {
      const text = skill.textContent.toLowerCase();
      skill.style.display = text.includes(query) ? 'block' : 'none';
    });
  });

  // Task 8
  const passInput = document.getElementById('passInput');
  const togglePass = document.getElementById('togglePass');
  const passStrength = document.getElementById('passStrength');

  togglePass.addEventListener('click', () => {
    const isPassword = passInput.getAttribute('type') === 'password';
    passInput.setAttribute('type', isPassword ? 'text' : 'password');
    togglePass.textContent = isPassword ? 'Hide' : 'Show';
  });

  passInput.addEventListener('input', () => {
    const val = passInput.value;
    const hasNumber = /\d/.test(val);

    if (val.length === 0) {
      passStrength.textContent = '';
    } else if (val.length >= 6 && hasNumber) {
      passStrength.textContent = 'Strong';
      passStrength.style.color = 'green';
    } else {
      passStrength.textContent = 'Weak';
      passStrength.style.color = 'red';
    }
  });

  // Task 9
  const openModal = document.getElementById('openModal');
  const closeModal = document.getElementById('closeModal');
  const modalOverlay = document.getElementById('modalOverlay');

  openModal.addEventListener('click', () => modalOverlay.classList.remove('hidden'));
  closeModal.addEventListener('click', () => modalOverlay.classList.add('hidden'));

  modalOverlay.addEventListener('click', (e) => {
    if (e.target === modalOverlay) {
      modalOverlay.classList.add('hidden');
    }
  });

  // Task 10
  const regForm = document.getElementById('regForm');
  const regSuccess = document.getElementById('regSuccess');

  regForm.addEventListener('submit', (e) => {
    e.preventDefault();
    let isValid = true;
    regSuccess.textContent = '';

    const inputs = [
      document.getElementById('regName'),
      document.getElementById('regEmail'),
      document.getElementById('regPass')
    ];

    inputs.forEach(input => {
      const errorSpan = input.nextElementSibling;
      if (input.value.trim() === '') {
        isValid = false;
        input.classList.add('error-border');
        errorSpan.textContent = 'Field required';
      } else {
        input.classList.remove('error-border');
        errorSpan.textContent = '';
      }
    });

    if (isValid) {
      regForm.reset();
      regSuccess.textContent = 'Registration successful!';
    }
  });
});