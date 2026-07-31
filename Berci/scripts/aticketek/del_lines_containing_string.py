file = 'c:/GIT/EMAP/emap-liquibase/liquibase/emap_gateway/tables/event_routing_catalog/0032-event_routing_catalog-delete_neak.sql'
with open(file, 'r', encoding='utf-8') as f:
    lines = f.readlines()
lines = [line for line in lines if 'NEAK' not in line]
with open(file, 'w', encoding='utf-8') as f:
    f.writelines(lines)