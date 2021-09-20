from cohortextractor import StudyDefinition, patients, codelist, codelist_from_csv  # NOQA


study = StudyDefinition(
    default_expectations={
        "date": {"earliest": "1900-01-01", "latest": "today"},
        "rate": "uniform",
        "incidence": 0.5,
    },

    index_date = "2020-10-01",

    population=patients.satisfying(
        """registered AND
        age>18 AND
        age<30""",
    
        registered = patients.registered_with_one_practice_between(
            "2019-02-01", "index_date"
        ),

        age = patients.age_as_of(
            "index_date"
        )
    ),

    practice_enrolled=patients.registered_practice_as_of(
        "index_date",
        returning="rct__germdefence__enrolled",
        return_expectations={
            "incidence": 0.4,
        },
    ),

    practice_trial_arm=patients.registered_practice_as_of(
        "index_date",
        returning="rct__germdefence__trial_arm",
        return_expectations={
            "rate": "universal",
            "category": {
                "ratios": {
                    "con": 0.5,
                    "int": 0.5
                },
            },
        },
    ),

    practice_deprivation_pctile=patients.registered_practice_as_of(
        "index_date",
        returning="rct__germdefence__deprivation_pctile",
        return_expectations={
            "rate": "universal",
            "category": {
                "ratios": {
                    "1": 0.5,
                    "2": 0.5
                },
            },
        },
    )
)
