# liquibase_runner #
A program lefuttatja a megadott repository szkriptjeit a megadott környezeteken.
A repository paraméter egy lista.
A loc paraméter a környezetet adja meg, ahol futtatni szeretnénk.

A loc lehetséges értékei:
* 'local'
* 'sandbox'
* 'dev'
* 'fit'
* 'perf'
* 'remote'
  * 'sandbox'
  * 'dev'
  * 'fit'

Ez azonban csak a következő auth proxy beállításokkal működik:
* local = 5432
* start cmd /kcloud_sql_proxy_x64.exe -instances=mlff-sb:europe-west1:sb-man-db=tcp:5433
* start cmd /kcloud_sql_proxy_x64.exe - nstances=mlff-dev:europe-west1:mlff-dev-postgre-1-c54aaddd=tcp:5434
* start cmd /kcloud_sql_proxy_x64.exe -instances=mlff-fit:europe-west1:mlff-fit-postgre-1-037a04b9=tcp:5435
* cloud_sql_proxy_x64.exe -instances=mlff-perf:europe-west1:mlff-perf-postgre-1-111557c9=tcp:5436



