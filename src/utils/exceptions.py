class ETLException(Exception):
    """Base exception for ETL pipeline"""
    pass # inherits everything from Eception



class ExtractionError(ETLException):
    """Raised when data extraction fails"""
    pass



class TransformationError(ETLException):
    """Raised when data transformation fails"""
    pass



class LoadError(ETLException):
    """Raised when loading to database fails"""
    pass



class ValidationError(ETLException):
    """Raised when data validation fails"""
    pass