from gyrus import Context, Processor, State


class Node(Processor):
    async def process(self, ctx: Context, state: State) -> bool:
        print("this is processor_context")

        from_b = state.get("context_from_case_b", 0)
        from_c = state.get("context_from_case_c", 0)

        if ctx.parent == "case_b":
            state.set("context_from_case_b", from_b + 1)

        if ctx.parent == "case_c":
            state.set("context_from_case_c", from_c + 1)

        state.set("object_in_context", ctx.object_in_context)
        return True
