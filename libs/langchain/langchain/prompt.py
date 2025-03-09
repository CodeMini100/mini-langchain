import string

class PromptTemplate:
    def __init__(self, template: str):
        """
        Initialize the prompt template.
        TODO: Validate the template format.
        Hint: Check if '$' exists for variable placeholders.
        """
        pass

    def render(self, **kwargs) -> str:
        """
        Render the prompt with provided variables.
        TODO:
          - Substitute variables using string.Template.
          - Validate that all required keys are provided.
          - Log any missing variables.
        Hint: Use:
            tmpl = string.Template(self.template)
            return tmpl.safe_substitute(**kwargs)
        """
        pass
