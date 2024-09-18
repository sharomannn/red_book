class CATEGORY:
    """Категория"""

    CATEGORY_CHOICES = [
        ('1', 'Вымирающие виды'),
        ('2', 'Уязвимые виды'),
        ('3', 'Редкие виды'),
        ('4', 'Неопределенные виды'),
        ('5', 'Восстанавливающиеся виды'),
    ]

    ENDANGERED_SPECIES = '1'
    VULNERABLE_SPECIES = '2'
    RARE_SPECIES = '3'
    UNKNOWN_SPECIES = '4'
    RECOVERING_SPECIES = '5'

    ENDANGERED_SPECIES_RUS = 'Вымирающие виды'
    VULNERABLE_SPECIES_RUS = 'Уязвимые виды'
    RARE_SPECIES_RUS = 'Редкие виды'
    UNKNOWN_SPECIES_RUS = 'Неопределенные виды'
    RECOVERING_SPECIES_RUS = 'Восстанавливающиеся виды'

    CHOICES = (
        (ENDANGERED_SPECIES, ENDANGERED_SPECIES_RUS),
        (VULNERABLE_SPECIES, VULNERABLE_SPECIES_RUS),
        (RARE_SPECIES, RARE_SPECIES_RUS),
        (UNKNOWN_SPECIES, UNKNOWN_SPECIES_RUS),
        (RECOVERING_SPECIES, RECOVERING_SPECIES_RUS),
    )