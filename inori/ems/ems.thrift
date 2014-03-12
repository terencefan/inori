# define ems service
namespace py ems

/**
 * Exceptions
 */
enum EMSErrorCode {
    UNKNOWN_ERROR,

    // User Errors
    SEND_TIMEOUT,

    // System Errors
    DATABASE_ERROR,
}

exception EMSUserException {
    1: required EMSErrorCode error_code,
    2: required string error_name,
    3: optional string message,
}

exception EMSSystemException {
    1: required EMSErrorCode error_code,
    2: required string error_name,
    3: optional string message,
}

exception EMSUnknownException {
    1: required EMSErrorCode error_code,
    2: required string error_name,
    3: required string message,
}

/**
 * Types and Structs
 */
typedef string EmailAddress
typedef i64 Timestamp

/**
 * Services
 */
service EmailService {
    /**
     * Base APIs
     */
    bool ping()
        throws(1: EMSUserException user_exception,
               2: EMSSystemException system_exception,
               3: EMSUnknownException unknown_exception),

    void send(1: EmailAddress sender,
              2: EmailAddress receiver,
              3: string title,
              4: string content)
        throws(1: EMSUserException user_exception,
               2: EMSSystemException system_exception,
               3: EMSUnknownException unknown_exception),

    void set_messager(1: string name)
        throws(1: EMSUserException user_exception,
               2: EMSSystemException system_exception,
               3: EMSUnknownException unknown_exception),

    /**
     * Inner APIs
     */
    void process_send(1: i32 email_id)
        throws(1: EMSUserException user_exception,
               2: EMSSystemException system_exception,
               3: EMSUnknownException unknown_exception),
}
