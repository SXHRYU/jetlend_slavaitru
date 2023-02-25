# С лямбдой
from typing import Callable, Any, TypeAlias

T_callable: TypeAlias = Callable[[int], Any]


def create_handlers(callback: T_callable) -> list[T_callable]:
    handlers: list[T_callable] = []
    for step in range(5):
        # добавляем обработчики для каждого шага
        handlers.append(lambda i=step: callback(i))  # type: ignore
    return handlers


def execute_handlers(handlers: list[T_callable]) -> None:
    # запускаем добавленные обработчики
    for handler in handlers:
        handler()  # type: ignore


def f1(reps: int) -> str:
    return "hi" * reps


execute_handlers(create_handlers(f1))
