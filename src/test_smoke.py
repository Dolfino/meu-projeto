import os
import requests
import pytest
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

# Configurações baseadas no ambiente
ENVIRONMENT = os.getenv('ENVIRONMENT', 'development')
BASE_URL = os.getenv(
    'PRODUCTION_URL' if ENVIRONMENT == 'production' else 'LOCAL_URL'
)
TIMEOUT = 10  # segundos
MAX_RETRIES = 3

# Configuração de retry para requests
session = requests.Session()
retry_strategy = Retry(
    total=MAX_RETRIES,
    backoff_factor=1,
    status_forcelist=[500, 502, 503, 504]
)
adapter = HTTPAdapter(max_retries=retry_strategy)
session.mount("http://", adapter)
session.mount("https://", adapter)


@pytest.mark.smoke
class TestHealthChecks:
    """Testes críticos de saúde do sistema"""

    def test_health_endpoint(self):
        """Verifica se o endpoint /healthz retorna status 200"""
        try:
            response = session.get(
                f"{BASE_URL}/healthz",
                timeout=TIMEOUT
            )
            assert response.status_code == 200, (
                f"Endpoint /healthz retornou {response.status_code}. "
                f"Resposta: {response.text}"
            )
            assert response.json() == {"status": "ok"}, (
                "Resposta JSON inesperada do endpoint /healthz"
            )
        except requests.exceptions.RequestException as e:
            pytest.fail(f"Falha ao acessar /healthz: {str(e)}")

    def test_ready_endpoint(self):
        """Verifica se o endpoint /readyz retorna status 200"""
        try:
            response = session.get(
                f"{BASE_URL}/readyz",
                timeout=TIMEOUT
            )
            assert response.status_code == 200, (
                f"Endpoint /readyz retornou {response.status_code}. "
                f"Resposta: {response.text}"
            )
            assert response.json() == {"status": "ready"}, (
                "Resposta JSON inesperada do endpoint /readyz"
            )
        except requests.exceptions.RequestException as e:
            pytest.fail(f"Falha ao acessar /readyz: {str(e)}")


@pytest.mark.smoke
@pytest.mark.critical
class TestCriticalEndpoints:
    """Testes de endpoints críticos da aplicação"""

    def test_main_api_endpoint(self):
        """Verifica se o endpoint principal da API está acessível"""
        try:
            response = session.get(
                f"{BASE_URL}/api/v1/",
                timeout=TIMEOUT
            )
            assert response.status_code == 200, (
                f"Endpoint principal retornou {response.status_code}. "
                f"Resposta: {response.text}"
            )
        except requests.exceptions.RequestException as e:
            pytest.fail(f"Falha ao acessar endpoint principal: {str(e)}")

    def test_database_connection(self):
        """Verifica se a conexão com o banco de dados está funcionando"""
        try:
            response = session.get(
                f"{BASE_URL}/api/v1/db-check",
                timeout=TIMEOUT
            )
            assert response.status_code == 200, (
                f"Endpoint db-check retornou {response.status_code}. "
                f"Resposta: {response.text}"
            )
            status = response.json().get("status", "").lower()
            assert "connected" in status, (
                f"Status inesperado da conexão com o banco: {status}"
            )
        except requests.exceptions.RequestException as e:
            pytest.fail(f"Falha ao verificar conexão com banco: {str(e)}")


@pytest.mark.smoke
class TestConfigurationValidation:
    """Testes de validação de configuração do sistema"""

    def test_environment_variables(self):
        """Verifica se as variáveis de ambiente
        essenciais estão configuradas"""
        required_vars = [
            'DB_HOST', 'DB_PORT', 'DB_NAME',
            'SECRET_KEY', 'PRODUCTION_URL', 'LOCAL_URL'
        ]

        missing_vars = [var for var in required_vars if not os.getenv(var)]
        assert not missing_vars, (
            "Variáveis de ambiente obrigatórias não configuradas: "
            f"{', '.join(missing_vars)}"
        )

    @pytest.mark.flaky(reruns=2, reruns_delay=1)
    def test_third_party_services(self):
        """Verifica conexão com serviços externos essenciais"""
        try:
            response = session.get(
                f"{BASE_URL}/api/v1/external-service-check",
                timeout=TIMEOUT
            )
            assert response.status_code == 200, (
                "Verificação de serviço externo retornou "
                f"{response.status_code}. "
                f"Resposta: {response.text}"
            )
        except requests.exceptions.RequestException as e:
            pytest.fail(f"Falha ao verificar serviço externo: {str(e)}")
