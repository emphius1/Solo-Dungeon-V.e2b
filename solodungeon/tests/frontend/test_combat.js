import React from 'react';
import { render, fireEvent, screen } from '@testing-library/react';
import Combat from '../../src/components/Combat';
import { combatSchema } from '../../src/sharedDependencies';

describe('Combat Component', () => {
  test('renders combat interface', () => {
    render(<Combat />);
    const combatInterface = screen.getByTestId('combat-interface');
    expect(combatInterface).toBeInTheDocument();
  });

  test('executes combat action', () => {
    const { getByText } = render(<Combat />);
    const attackButton = getByText(/attack/i);
    fireEvent.click(attackButton);
    expect(combatSchema.executeCombat).toHaveBeenCalled();
  });

  test('updates combat state', () => {
    const { getByText } = render(<Combat />);
    const defendButton = getByText(/defend/i);
    fireEvent.click(defendButton);
    expect(combatSchema.updateCombatState).toHaveBeenCalled();
  });

  test('displays combat log', () => {
    render(<Combat />);
    const combatLog = screen.getByTestId('combat-log');
    expect(combatLog).toHaveTextContent(/combat started/i);
  });

  test('handles AI response', () => {
    render(<Combat />);
    const aiResponse = screen.getByTestId('ai-response');
    expect(aiResponse).toHaveTextContent(/enemy attacks/i);
  });
});