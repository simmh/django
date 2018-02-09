# 일반적으로 장고로부터 직접 무언가를 설정 파일로 임포트해 올 일은
# 없을 것이며 또한 해서도 안 된다 . 단 ImproperyConfigured 는 예외다 .
from django.core.exceptions import ImproperlyConfigured
# JSON 기반 비밀 모듈
with open("secrets.json") as f:
secrets = json.loads(f.read())


def get _ secret(setting, secrets=secrets):

""" 비밀 변수를 가져오거나 명시적 예외를 반환한다 ."""
try:
return secrets[setting]
except KeyError:
error _ msg = "Set the {0} environment variable".format(setting)
