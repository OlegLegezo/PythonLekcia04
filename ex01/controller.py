import modelMult as model1
import modelSum as model2
import view


def buttonClick():
    valueA = view.getValue()
    valueB = view.getValue()
    model1.init(valueA, valueB)
    result = model1.doIt()
    view.viewData(result, "mul")
    model2.init(valueA, valueB)
    result = model2.doIt()
    view.viewData(result, "sum")
