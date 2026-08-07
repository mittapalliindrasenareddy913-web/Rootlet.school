// ==========================================================================
// ROOTLET PRESCHOOL - MAIN JAVASCRIPT LOGIC
// ==========================================================================

document.addEventListener('DOMContentLoaded', () => {
  // Modal Elements
  const modalOverlay = document.getElementById('modalOverlay');
  const modalCloseBtn = document.getElementById('modalClose');
  const openModalBtns = document.querySelectorAll('.open-modal-btn');
  const heroForm = document.getElementById('heroForm');
  const popupForm = document.getElementById('popupForm');
  const heroHeader = document.querySelector('.hero-header');

  // WhatsApp Target Phone Number: 8867672627
  const WHATSAPP_NUMBER = '918867672627';

  // 1. SMART SCROLL: HIDE ON SCROLL DOWN, REVEAL ON SCROLL UP / REVERSE / STOP
  let lastScrollY = window.scrollY;

  window.addEventListener('scroll', () => {
    const currentScrollY = window.scrollY;

    // Only hide if scrolled down past 120px
    if (currentScrollY > 120 && currentScrollY > lastScrollY) {
      // Scrolling DOWN -> hide header
      if (heroHeader) {
        heroHeader.classList.add('header-hidden');
      }
    } else {
      // Scrolling UP or at top -> show header
      if (heroHeader) {
        heroHeader.classList.remove('header-hidden');
      }
    }

    lastScrollY = currentScrollY;
  });

  // Open Modal & Auto-Select Program
  openModalBtns.forEach(btn => {
    btn.addEventListener('click', (e) => {
      e.preventDefault();
      const prog = btn.getAttribute('data-program');
      if (prog && popupForm) {
        const select = popupForm.querySelector('select');
        if (select) {
          select.value = prog;
        }
      }
      if (modalOverlay) {
        modalOverlay.classList.add('active');
      }
    });
  });

  // Close Modal
  if (modalCloseBtn) {
    modalCloseBtn.addEventListener('click', () => {
      modalOverlay.classList.remove('active');
    });
  }

  // Close modal when clicking outside card
  if (modalOverlay) {
    modalOverlay.addEventListener('click', (e) => {
      if (e.target === modalOverlay) {
        modalOverlay.classList.remove('active');
      }
    });
  }

  // Helper function to extract form values and build full WhatsApp URL
  const buildWhatsAppUrl = (form, headingText) => {
    const parentName = form.elements['parentName']?.value || form.querySelector('input[type="text"]')?.value || '';
    const email = form.elements['email']?.value || form.querySelector('input[type="email"]')?.value || '';
    const phone = form.elements['phone']?.value || form.querySelector('input[type="tel"]')?.value || '';
    const dob = form.elements['dob']?.value || '';
    const program = form.elements['program']?.value || form.querySelector('select')?.value || '';

    const textMessage = `${headingText}\n\n` +
      `👤 *Parent / Guardian Name:* ${parentName}\n` +
      `📧 *Email Address:* ${email}\n` +
      `📞 *Phone Number:* ${phone}\n` +
      `👶 *Child's Date of Birth:* ${dob}\n` +
      `🏫 *Programme of Interest:* ${program}`;

    return `https://wa.me/${WHATSAPP_NUMBER}?text=${encodeURIComponent(textMessage)}`;
  };

  // 2. HERO ENQUIRY FORM SUBMISSION -> WHATSAPP REDIRECT
  if (heroForm) {
    heroForm.addEventListener('submit', (e) => {
      e.preventDefault();

      const whatsappUrl = buildWhatsAppUrl(heroForm, 'Hello Rootlet Preschool! I would like to make an enquiry:');
      window.open(whatsappUrl, '_blank');
      heroForm.reset();
    });
  }

  // 3. POPUP FORM SUBMISSION -> WHATSAPP REDIRECT
  if (popupForm) {
    popupForm.addEventListener('submit', (e) => {
      e.preventDefault();

      const whatsappUrl = buildWhatsAppUrl(popupForm, 'Hello Rootlet Preschool! I would like to make an Enquiry & Admission request:');
      window.open(whatsappUrl, '_blank');

      if (modalOverlay) {
        modalOverlay.classList.remove('active');
      }
      popupForm.reset();
    });
  }

  // 4. MOBILE DRAWER NAVIGATION TOGGLE
  const mobileMenuBtn = document.getElementById('mobileMenuBtn');
  const mobileNavDrawer = document.getElementById('mobileNavDrawer');
  const drawerCloseBtn = document.getElementById('drawerCloseBtn');
  const drawerNavLinks = document.querySelectorAll('.drawer-nav-link');

  if (mobileMenuBtn && mobileNavDrawer) {
    mobileMenuBtn.addEventListener('click', (e) => {
      e.preventDefault();
      e.stopPropagation();
      mobileNavDrawer.classList.add('active');
    });
  }

  if (drawerCloseBtn && mobileNavDrawer) {
    drawerCloseBtn.addEventListener('click', () => {
      mobileNavDrawer.classList.remove('active');
    });
  }

  drawerNavLinks.forEach(link => {
    link.addEventListener('click', () => {
      if (mobileNavDrawer) {
        mobileNavDrawer.classList.remove('active');
      }
    });
  });
});
