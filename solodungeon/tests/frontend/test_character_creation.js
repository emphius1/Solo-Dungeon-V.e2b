import React from 'react';
import { render, screen, fireEvent } from '@testing-library/react';
import '@testing-library/jest-dom/extend-expect';
import CharacterCreation from '../../src/components/CharacterCreation';

describe('Character Creation Component Tests', () => {
  test('renders CharacterCreation component', () => {
    render(<CharacterCreation />);
    expect(screen.getByTestId('character-creation-form')).toBeInTheDocument();
  });

  test('allows users to input character name', () => {
    render(<CharacterCreation />);
    const nameInput = screen.getByLabelText(/character name/i);
    fireEvent.change(nameInput, { target: { value: 'Aragorn' } });
    expect(nameInput.value).toBe('Aragorn');
  });

  test('allows users to select character class', () => {
    render(<CharacterCreation />);
    const classSelect = screen.getByLabelText(/character class/i);
    fireEvent.change(classSelect, { target: { value: 'Ranger' } });
    expect(classSelect.value).toBe('Ranger');
  });

  test('allows users to select character race', () => {
    render(<CharacterCreation />);
    const raceSelect = screen.getByLabelText(/character race/i);
    fireEvent.change(raceSelect, { target: { value: 'Human' } });
    expect(raceSelect.value).toBe('Human');
  });

  test('submits the form and calls the createCharacter function', () => {
    const mockCreateCharacter = jest.fn();
    render(<CharacterCreation createCharacter={mockCreateCharacter} />);
    const submitButton = screen.getByRole('button', { name: /create character/i });
    fireEvent.click(submitButton);
    expect(mockCreateCharacter).toHaveBeenCalled();
  });
});