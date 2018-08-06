-- Revert lift:appschema from pg

BEGIN;

DROP SCHEMA lift_tracking;

COMMIT;
