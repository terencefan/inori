# define ems service
namespace py ems

/**
 * Exceptions
 */
enum EMSErrorCode {
    UNKNOWN_ERROR,

    // User Errors

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
}
