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

  // Open Modal
  openModalBtns.forEach(btn => {
    btn.addEventListener('click', (e) => {
      e.preventDefault();
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

  // 2. HERO ENQUIRY FORM SUBMISSION -> WHATSAPP REDIRECT
  if (heroForm) {
    heroForm.addEventListener('submit', (e) => {
      e.preventDefault();

      const inputs = heroForm.querySelectorAll('.form-input-control');
      const parentName = inputs[0]?.value || '';
      const email = inputs[1]?.value || '';
      const phone = inputs[2]?.value || '';
      const dob = inputs[3]?.value || '';
      const program = inputs[4]?.value || '';

      // Construct formatted WhatsApp message
      const textMessage = `Hello Rootlet Preschool! I would like to enquire about enrolment:%0A%0A` +
        `*Parent Name:* ${encodeURIComponent(parentName)}%0A` +
        `*Email:* ${encodeURIComponent(email)}%0A` +
        `*Phone:* ${encodeURIComponent(phone)}%0A` +
        `*Child DOB:* ${encodeURIComponent(dob)}%0A` +
        `*Program:* ${encodeURIComponent(program)}`;

      const whatsappUrl = `https://wa.me/${WHATSAPP_NUMBER}?text=${textMessage}`;

      // Open WhatsApp in new tab
      window.open(whatsappUrl, '_blank');

      heroForm.reset();
    });
  }

  // 3. POPUP FORM SUBMISSION -> WHATSAPP REDIRECT
  if (popupForm) {
    popupForm.addEventListener('submit', (e) => {
      e.preventDefault();

      const inputs = popupForm.querySelectorAll('.form-input-control');
      const parentName = inputs[0]?.value || '';
      const phone = inputs[1]?.value || '';
      const program = inputs[2]?.value || '';

      const textMessage = `Hello Rootlet Preschool! I would like to schedule a visit / enquiry:%0A%0A` +
        `*Parent Name:* ${encodeURIComponent(parentName)}%0A` +
        `*Phone:* ${encodeURIComponent(phone)}%0A` +
        `*Program:* ${encodeURIComponent(program)}`;

      const whatsappUrl = `https://wa.me/${WHATSAPP_NUMBER}?text=${textMessage}`;

      // Open WhatsApp in new tab
      window.open(whatsappUrl, '_blank');

      if (modalOverlay) {
        modalOverlay.classList.remove('active');
      }
      popupForm.reset();
    });
  }
});
