import os
import pytest
from config import load_config, get_database_url

# -----------------------------------------------------------------------------
# Test Suite for config.py
# This test file covers:
#     1. load_config() - Ensures environment variables or .env values are loaded
#     2. get_database_url() - Returns a valid SQLAlchemy connection string
# -----------------------------------------------------------------------------

@pytest.mark.describe("load_config() function tests")
class TestLoadConfig:
    # -------------------------------------------------------------------------
    # Test: Verifying that load_config() picks up environment variables.
    #       We mock two environment variables and check if the returned config
    #       contains them as expected.
    # -------------------------------------------------------------------------
    @pytest.mark.it("Should load environment variables into a config object")
    def test_load_config_with_env(self, monkeypatch):
        monkeypatch.setenv("TEST_VAR_1", "value1")
        monkeypatch.setenv("TEST_VAR_2", "value2")

        config = load_config()

        assert config is not None, "Expected load_config() to return a config object, got None"
        assert "TEST_VAR_1" in config, "Expected TEST_VAR_1 to be in the returned config"
        assert "TEST_VAR_2" in config, "Expected TEST_VAR_2 to be in the returned config"
        assert config["TEST_VAR_1"] == "value1", "Unexpected value for TEST_VAR_1"
        assert config["TEST_VAR_2"] == "value2", "Unexpected value for TEST_VAR_2"

    # -------------------------------------------------------------------------
    # Test: If no environment variables are set, load_config() should not fail
    #       and could return an empty dict or default values. This test ensures
    #       the function handles missing env gracefully.
    # -------------------------------------------------------------------------
    @pytest.mark.it("Should gracefully handle when environment variables are not set")
    def test_load_config_without_env(self, monkeypatch):
        # Clear environment variables that might interfere
        monkeypatch.delenv("TEST_VAR_1", raising=False)
        monkeypatch.delenv("TEST_VAR_2", raising=False)

        config = load_config()

        assert config is not None, "Function should still return a config object even if no env is set"
        # We do not expect TEST_VAR_1 or TEST_VAR_2 in config now
        assert "TEST_VAR_1" not in config, "TEST_VAR_1 should not be present"
        assert "TEST_VAR_2" not in config, "TEST_VAR_2 should not be present"


@pytest.mark.describe("get_database_url() function tests")
class TestGetDatabaseUrl:
    # -------------------------------------------------------------------------
    # Test: Mock environment variables required for constructing a DB URL
    #       and ensure get_database_url() returns the correct format.
    # -------------------------------------------------------------------------
    @pytest.mark.it("Should return the correct SQLAlchemy URL when environment variables are set")
    def test_get_database_url_with_valid_env(self, monkeypatch):
        monkeypatch.setenv("DB_USER", "testuser")
        monkeypatch.setenv("DB_PASSWORD", "testpass")
        monkeypatch.setenv("DB_HOST", "localhost")
        monkeypatch.setenv("DB_PORT", "5432")
        monkeypatch.setenv("DB_NAME", "testdb")

        db_url = get_database_url()
        expected_url = "postgresql://testuser:testpass@localhost:5432/testdb"
        assert db_url == expected_url, f"Expected {expected_url}, got {db_url}"

    # -------------------------------------------------------------------------
    # Test: When required env variables are missing, get_database_url() may
    #       return a default or raise an error. Adjust assertions based on
    #       expected behavior in your implementation.
    # -------------------------------------------------------------------------
    @pytest.mark.it("Should handle missing DB environment variables gracefully")
    def test_get_database_url_missing_env(self, monkeypatch):
        monkeypatch.delenv("DB_USER", raising=False)
        monkeypatch.delenv("DB_PASSWORD", raising=False)
        monkeypatch.delenv("DB_HOST", raising=False)
        monkeypatch.delenv("DB_PORT", raising=False)
        monkeypatch.delenv("DB_NAME", raising=False)

        # Depending on implementation, this might return None, a default URL, or raise an exception.
        # If an exception is expected, use pytest.raises(ExceptionName):
        #     with pytest.raises(SomeExceptionType):
        #         get_database_url()
        #
        # For demonstration, we assume it returns None or an empty string if missing.
        db_url = get_database_url()
        assert db_url is not None, "Expected a fallback or empty string instead of None"
        assert db_url != "", "Expected a fallback database URL instead of an empty string"