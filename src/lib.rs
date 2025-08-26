mod factory;
mod number;
mod utils;

use pyo3::prelude::*;

use crate::{factory::DeterministicFunnyNumberFactory, number::FunnyNumber};

#[pymodule]
fn _core(m: &Bound<'_, PyModule>) -> PyResult<()> {
    m.add_class::<FunnyNumber>()?;
    m.add_class::<DeterministicFunnyNumberFactory>()?;
    Ok(())
}
