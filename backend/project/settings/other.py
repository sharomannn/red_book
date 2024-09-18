import datetime

CORS_ORIGIN_WHITELIST = [
    'http://localhost:8080',
    'http://localhost:8081',
    'http://localhost:8082',
    'http://localhost:8083',
    'http://localhost:8084',
    'http://localhost:8085',
]

SPECTACULAR_SETTINGS = {
    'TITLE': 'Красная книга',
    'VERSION': 1.0,
    'DESCRIPTION': f'Время пуска сервера (UTC): {datetime.datetime.now(tz=datetime.timezone.utc):%d %B %H:%M}',
    # Не показывать ручку получения схемы
    'SERVE_INCLUDE_SCHEMA': False,
    # Для интеграции с drf-spectacular
    'ENUM_NAME_OVERRIDES': {
        'ValidationErrorEnum': 'drf_standardized_errors.openapi_serializers.ValidationErrorEnum.choices',
        'ClientErrorEnum': 'drf_standardized_errors.openapi_serializers.ClientErrorEnum.choices',
        'ServerErrorEnum': 'drf_standardized_errors.openapi_serializers.ServerErrorEnum.choices',
        'ErrorCode401Enum': 'drf_standardized_errors.openapi_serializers.ErrorCode401Enum.choices',
        'ErrorCode403Enum': 'drf_standardized_errors.openapi_serializers.ErrorCode403Enum.choices',
        'ErrorCode404Enum': 'drf_standardized_errors.openapi_serializers.ErrorCode404Enum.choices',
        'ErrorCode405Enum': 'drf_standardized_errors.openapi_serializers.ErrorCode405Enum.choices',
        'ErrorCode406Enum': 'drf_standardized_errors.openapi_serializers.ErrorCode406Enum.choices',
        'ErrorCode415Enum': 'drf_standardized_errors.openapi_serializers.ErrorCode415Enum.choices',
        'ErrorCode429Enum': 'drf_standardized_errors.openapi_serializers.ErrorCode429Enum.choices',
        'ErrorCode500Enum': 'drf_standardized_errors.openapi_serializers.ErrorCode500Enum.choices',
    },
    # Для интеграции с drf-spectacular
    'POSTPROCESSING_HOOKS': ['drf_standardized_errors.openapi_hooks.postprocess_schema_enums'],
}
