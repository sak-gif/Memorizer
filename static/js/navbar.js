const bar = document.getElementById('bars');
const ROUTES = {
    home: "{{ url_for('home') }}"
  };
const navbar = `
  <div class="navcontainer" id="navbarcontainer">
    <i class="fa-solid fa-xmark" id="close-nav" style="cursor: pointer;"></i>

    <div class="user-profile">
      <i class="fa-solid fa-circle-user"></i>
      <span id="username">محمد محمود</span>
    </div>
    <div class="nav-labels">
      <a href=''>الرئيسية</a>
      <a href="#">مجموعاتي</a>
      <i class="fa-solid fa-right-from-bracket"></i>
    </div>
  </div>
`;

document.body.insertAdjacentHTML('beforeend', navbar);

const nav = document.getElementById('navbarcontainer');
const closeBtn = document.getElementById('close-nav');

bar.addEventListener('click', () => {
  nav.classList.add('open');
});

closeBtn.addEventListener('click', () => {
  nav.classList.remove('open');
});