-- Verify lift:appschema on pg

BEGIN;

SELECT pg_catalog.has_schema_privilege('lift_tracking', 'usage');

ROLLBACK;
