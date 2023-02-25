# Без лямбды
from typing import Any, Callable


class Callback:
    def __init__(
        self, callback: Callable[[Any], Any], *args: Any, **kwargs: Any
    ) -> None:
        self.callback: Callable[[Any], Any] = callback
        self.args: tuple[Any, ...] = args
        self.kwargs: dict[Any, Any] = kwargs

    def __call__(self) -> Any:
        return self.callback(*self.args, **self.kwargs)


def create_handlers(callback: Callable[[int], Any]) -> list[Callback]:
    handlers: list[Callback] = []
    for step in range(5):
        # добавляем обработчики для каждого шага
        handlers.append(Callback(callback, step))
    return handlers


def execute_handlers(handlers: list[Callback]) -> None:
    # запускаем добавленные обработчики
    for handler in handlers:
        handler()


def f1(reps: int) -> str:
    return "hi" * reps


execute_handlers(create_handlers(f1))
