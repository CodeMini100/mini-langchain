import pytest
from unittest.mock import patch, MagicMock
from tools.tools_service import search_tool, calculator_tool


@pytest.mark.describe("Tools Service - search_tool function")
class TestSearchTool:
    # -------------------------------------------------------------------------
    # Test a successful search with a normal query
    # -------------------------------------------------------------------------
    @pytest.mark.it("Should return valid search results for a non-empty query")
    def test_search_tool_success(self):
        query = "sample query"
        # Mock or assume the function returns a list of results or similar data
        # For demonstration, we don't patch any external call since none is specified
        result = search_tool(query)
        assert result is not None, "Expected a result from search_tool"
        # This assertion depends on what the function actually returns
        # Adjust accordingly to match expected shape of the result
        assert isinstance(result, list) or isinstance(result, str), (
            "Expected search_tool() to return a list or string of results"
        )

    # -------------------------------------------------------------------------
    # Test how the function behaves when given an empty query
    # -------------------------------------------------------------------------
    @pytest.mark.it("Should handle empty or invalid queries gracefully")
    def test_search_tool_empty_query(self):
        query = ""
        result = search_tool(query)
        # Depending on logic, it might return an empty list, None, or raise an exception.
        # Adjust this test to match actual behavior.
        assert result is not None, "search_tool() should return a non-None response for an empty query"
    
    # -------------------------------------------------------------------------
    # Test if an exception is raised or handled for invalid input
    # (Adjust this test if the function does not raise exceptions for invalid input)
    # -------------------------------------------------------------------------
    @pytest.mark.it("Should handle or raise an error for invalid input")
    def test_search_tool_invalid_input(self):
        # Example invalid input might be None or a wrong type
        with pytest.raises(TypeError):
            search_tool(None)


@pytest.mark.describe("Tools Service - calculator_tool function")
class TestCalculatorTool:
    # -------------------------------------------------------------------------
    # Test a valid mathematical expression
    # -------------------------------------------------------------------------
    @pytest.mark.it("Should correctly evaluate a valid mathematical expression")
    def test_calculator_tool_valid_expression(self):
        expression = "2 + 3 * 4"
        result = calculator_tool(expression)
        assert result == 14, "Expected calculator_tool to evaluate '2 + 3 * 4' to 14"

    # -------------------------------------------------------------------------
    # Test an expression that could lead to errors (like syntax errors)
    # -------------------------------------------------------------------------
    @pytest.mark.it("Should handle invalid expressions gracefully or raise an exception")
    def test_calculator_tool_invalid_expression(self):
        expression = "2 + * 3"
        with pytest.raises(Exception):
            calculator_tool(expression)

    # -------------------------------------------------------------------------
    # Test handling of division by zero if applicable
    # -------------------------------------------------------------------------
    @pytest.mark.it("Should handle division by zero appropriately")
    def test_calculator_tool_division_by_zero(self):
        expression = "10 / 0"
        with pytest.raises(ZeroDivisionError):
            calculator_tool(expression)

    # -------------------------------------------------------------------------
    # Test expression with parentheses
    # -------------------------------------------------------------------------
    @pytest.mark.it("Should correctly handle expressions with parentheses")
    def test_calculator_tool_parentheses(self):
        expression = "(2 + 3) * 4"
        result = calculator_tool(expression)
        assert result == 20, "Expected calculator_tool to evaluate '(2 + 3) * 4' to 20"