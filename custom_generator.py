from typing_extensions import override

from binding_generator import BindingGenerator


class BindingGeneratorExtension(BindingGenerator):
    @override
    def generate_engine_class_header(self, class_api, used_classes, fully_used_classes, use_template_get_node):
        result = super().generate_engine_class_header(
            class_api, used_classes, fully_used_classes, use_template_get_node
        )
        signals = []
        if "signals" in class_api:
            for signal_api in class_api["signals"]:
                name = signal_api["name"]
                signal_constant = "\tstatic constexpr char SIGNAL_" + name.upper() + '[] = "' + name + '";'
                signals.append(signal_constant)
            try:
                idx = result.index("public:") + 1
                for signal_const in signals:
                    result.insert(idx, signal_const)
                    idx += 1
            except ValueError:
                print("no public keyword found, not adding signals")
        return result
