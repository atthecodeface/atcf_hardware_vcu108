import cdl_desc
from cdl_desc import CdlModule, CdlSimVerilatedModule, CModel, CSrc

class Library(cdl_desc.Library):
    name="vcu108"
    pass

class VCU108Modules(cdl_desc.Modules):
    name = "vcu108"
    src_dir      = "cdl"
    tb_src_dir   = "tb_cdl"
    libraries = {"std":True, "apb":True}
    cdl_include_dirs = ["cdl"]
    export_dirs = cdl_include_dirs + [ src_dir ]
    modules = []
    modules += [ CdlModule("subsys_minimal") ]
    modules += [ CdlModule("vcu108_debug") ]
    modules += [ CdlModule("vcu108_riscv",   instance_types={"riscv_i32_minimal_generic":"riscv_i32_minimal"}, cdl_filename="vcu108_riscv_generic") ]
    modules += [ CdlModule("vcu108_riscv_3", instance_types={"riscv_i32_minimal_generic":"riscv_i32_minimal3"}, cdl_filename="vcu108_riscv_generic") ]
    modules += [ CdlModule("tb_vcu108_debug",   instance_types={"vcu108_generic":"vcu108_debug"},   cdl_filename="tb_vcu108_generic", src_dir=tb_src_dir) ]
    modules += [ CdlModule("tb_vcu108_riscv",   instance_types={"vcu108_generic":"vcu108_riscv"},   cdl_filename="tb_vcu108_generic", src_dir=tb_src_dir) ]
    modules += [ CdlModule("tb_vcu108_riscv_3", instance_types={"vcu108_generic":"vcu108_riscv_3"}, cdl_filename="tb_vcu108_generic", src_dir=tb_src_dir) ]
    pass

