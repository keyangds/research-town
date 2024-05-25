from research_town.utils.agent_prompter import model_prompting


def test_model_call() -> None:
    prompt = "Here is a high-level summarized trend of a research field Machine Learning. "
    # response = model_prompting("mistralai/Mixtral-8x7B-Instruct-v0.1", prompt)
    # test gpt-3.5 instead
    response = model_prompting("gpt-3.5-turbo", prompt)
    assert response is not None
    assert len(response) > 0
    assert len(response[0]) > 0