-- Deploy lift:workout_session to pg

BEGIN;

CREATE TABLE workout_session(
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4()

)

COMMIT;
