import { themeStyles } from './themes/medievalFantasyTheme.css';

export const applyThematicElements = () => {
  const elements = document.querySelectorAll('[data-theme="medieval-fantasy"]');

  elements.forEach(element => {
    element.classList.add(themeStyles.mainTheme);
  });
};

export const validateAccessibility = () => {
  const interactiveElements = document.querySelectorAll('button, a, input, select, textarea');

  interactiveElements.forEach(element => {
    if (!element.hasAttribute('aria-label') && !element.hasAttribute('aria-labelledby')) {
      console.warn(`Accessibility issue: ${element.tagName} does not have an aria-label or aria-labelledby attribute.`);
    }
  });
};