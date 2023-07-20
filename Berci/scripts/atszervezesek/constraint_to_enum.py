    enumlist = (
      'REGISTRATION',
      'PHONE_NUMBER_MODIFICATION',
      'AD_HOC_TICKET_PAYMENT_SUCCESS',
      'AD_HOC_TICKET_PAYMENT_FAILED',
      'TICKET_PAYMENT_SUCCESS',
      'TICKET_PAYMENT_FAILED',
      'TRIP_PAYMENT_FAILED',
      'TRIP_PAYMENT_SUCCESS',
      'APPROACH_TOLL_ROAD_SEG',
      'ENTER_CLOSED_SEG',
      'EXIT_CLOSED_SEG',
      'ENTER_OPEN_SEG',
      'CUSTOMER_DELETION',
      'EMAIL_REGISTRATION',
      'TRIP_PAYMENT_FAILED_GRACE',
      'PSP_SETTLEMENT_PERIOD_BO',
      'TRO_SETTLEMENT_PERIOD_BO',
      'TRO_SETTLEMENT_PERIOD_TRO',
      'PASSWORD_RESET_WHATSAPP',
      'PASSWORD_RESET_EMAIL',
      'OBSERVATION_EVENT_WHATSAPP',
      'OBSERVATION_EVENT_EMAIL',
      'JOURNEY_PAYMENT_FAILED',
      'JOURNEY_PAYMENT_SUCCESS',
      'SANCTION_REG_INCREASE_WHATSAPP',
      'SANCTION_REG_CREATE_WHATSAPP',
      'INVITATION_ACCEPTED',
      'INVITATION_RECEIVED',
      'SANCTION_REG_INCREASE_EMAIL',
      'SANCTION_REG_CREATE_EMAIL',
      'SANCTION_REG_INCREASE_PN',
      'SANCTION_REG_CREATE_PN',
      'ONSITE_ALERT',
      'REFRESH_TRIP',
      'START_TRIP_PARALLEL',
      'PROVIDER_CUSTOMER_BINDING',
      'INVOICE_STATUS_CHANGED_TO_FINAL',
      'SANCTION_REG_CREATE_PUSH_NOTIFICATION',
      'SANCTION_REG_INCREASE_PUSH_NOTIFICATION',
      'PAYMENT_METHOD_BOUND',
      'PAYMENT_METHOD_UNBOUND',
      'PAYMENT_METHOD_BIND_FAILED ',
      'PAYMENT_METHOD_UNBIND_FAILED')


def convert_to_enum_cmd(tablename, column, enumname):
    insert =  f"ALTER TABLE {tablename} ALTER COLUMN {column} TYPE {enumname} USING\n"
    insert += f"  CASE\n"
    for enum in enumlist:
        insert += f"    WHEN {column}='{enum}' THEN '{enum}'::{enumname} \n"
    insert += '  END;'
    return insert


def gen_column_comment(tablename, column, enumname):
    insert = f"COMMENT ON COLUMN {tablename}.{column} IS 'ENUM:"
    for enum in enumlist:
        insert += f"''{enum}'',"
    insert = insert[0:-1] + ")';"
    return insert


if __name__ == '__main__':
    tablename = 'event'
    column = 'event'
    enumname = 'event_name'
    print(convert_to_enum_cmd(tablename, column, enumname))
    print(gen_column_comment(tablename, column, enumname))
    print(gen_column_comment(tablename+'$hist', column, enumname))
