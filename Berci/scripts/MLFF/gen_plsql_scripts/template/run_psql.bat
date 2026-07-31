@SET PGPASSWORD={password}
psql -p {core} -U postgres -d {pass} -q -f core_commands.sql
psql -p {enforcement} -U postgres -d {pass} -q -f enforcement_commands.sql
psql -p {eobu} -U postgres -d {pass} -q -f eobu_commands.sql
psql -p {obu} -U postgres -d {pass} -q -f obu_commands.sql
psql -p {payment} -U postgres -d {pass} -q -f payment.sql
psql -p {settlement} -U postgres -d {pass} -q -f settlement_commands.sql
psql -p {doc} -U postgres -d {pass} -q -f doc_commands.sql