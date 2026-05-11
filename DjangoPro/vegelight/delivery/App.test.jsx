import { describe, it, expect } from 'vitest';
import { render, screen, fireEvent } from '@testing-library/react'; // ✅ added fireEvent
import "@testing-library/jest-dom"; // ✅ required for toBeInTheDocument
import App from './App';


describe("App component test suite", () => {
  it("should render heading text and calculate sum", () => {
    render(<App />);


    // ✅ Check heading
    expect(screen.getByText("Hello World")).toBeInTheDocument();


    // ✅ Get inputs
    const inputs = screen.getAllByRole("spinbutton");
    const button = screen.getByText("Calculate Sum");


    // ✅ Simulate user input
    fireEvent.change(inputs[0], { target: { value: "4" } });
    fireEvent.change(inputs[1], { target: { value: "6" } });


    // ✅ Click button
    fireEvent.click(button);


    // ✅ Check result
    expect(screen.getByText("Result: 10")).toBeInTheDocument();
  });
});