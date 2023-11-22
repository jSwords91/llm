import logging
from functools import wraps
from typing import Callable, Any, Dict, List
import pandas as pd

logging.basicConfig(level=logging.CRITICAL)

class PromptMan:
    def __init__(self):
        self.captured_data: List[Dict[str, Any]] = []
        self.logger = logging.getLogger(__name__)

    def capture_prompt(self, func: Callable) -> Callable:
        """
        Decorator to capture and store arguments and responses of the decorated function.

        Args:
            func (Callable): The function to be decorated.

        Returns:
            Callable: The wrapped function.
        """

        @wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            try:
                response = func(*args, **kwargs)
            except Exception as e:
                self.logger.error(f"Error in executing function {func.__name__}: {e}")
                raise

            try:
                arg_names = func.__code__.co_varnames[:func.__code__.co_argcount]
                all_args = dict(zip(arg_names, args))
                all_args.update(kwargs)

                model = all_args.get('model')
                temperature = all_args.get('temperature')
                max_tokens = all_args.get('max_tokens')
                system_role = all_args.get('system_role', '')
                user_content = all_args.get('user_content', '')
                response_content = response.choices[0].message.content if response.choices else None

                self.captured_data.append({
                    "model": model,
                    "temperature": temperature,
                    "max_tokens": max_tokens,
                    "user_content": user_content,
                    "system_role": system_role,
                    "response_content": response_content
                })

            except Exception as e:
                self.logger.error(f"Error in capturing data for function {func.__name__}: {e}")

            return response

        return wrapper

    def to_dataframe(self) -> pd.DataFrame:
        """
        Converts the captured data into a pandas DataFrame.

        Returns:
            pd.DataFrame: DataFrame containing the captured data.
        """
        return pd.DataFrame(self.captured_data)
