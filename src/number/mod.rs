pub mod list;

use pyo3::prelude::*;

#[pyclass]
#[derive(Clone)]
pub struct FunnyNumber {
    #[pyo3(get)]
    pub number: f64,

    #[pyo3(get)]
    pub reason: String,
}

#[pymethods]
impl FunnyNumber {
    #[new]
    fn new(number: f64, reason: String) -> Self {
        FunnyNumber { number, reason }
    }

    fn __repr__(&self) -> String {
        format!("FunnyNumber({}, {})", self.number, self.reason)
    }
}
