import logging
from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
from src.services.proxmox import get_vms, vm_action

router_vm = Router()

VM_ALIASES = {
    "100": "Service A",
    "101": "Service B",
}


@router_vm.message(Command("vms"))
async def cmd_vms(message: Message):
    vms = get_vms()
    if not vms:
        await message.answer("⚠️ VM не найдены")
        return

    lines = []
    for vm in vms:
        vmid = str(vm["vmid"])
        name = VM_ALIASES.get(vmid, f"VM {vmid}")
        status = "🟢" if vm["status"] == "running" else "🔴"
        lines.append(f"{status} <b>{name}</b> (id: {vmid})")

    await message.answer(
        f"🖥 <b>Список VM</b>\n\n" + "\n".join(lines),
        parse_mode="HTML"
    )


@router_vm.message(Command("start_vm"))
async def cmd_start_vm(message: Message):
    args = message.text.split()
    if len(args) < 2:
        await message.answer("Использование: /start_vm <id>")
        return
    vmid = args[1]
    name = VM_ALIASES.get(vmid, f"VM {vmid}")
    ok = vm_action(int(vmid), "start")
    await message.answer(
        f"✅ {name} запущена" if ok else f"❌ Ошибка запуска {name}"
    )


@router_vm.message(Command("stop_vm"))
async def cmd_stop_vm(message: Message):
    args = message.text.split()
    if len(args) < 2:
        await message.answer("Использование: /stop_vm <id>")
        return
    vmid = args[1]
    name = VM_ALIASES.get(vmid, f"VM {vmid}")
    ok = vm_action(int(vmid), "stop")
    await message.answer(
        f"✅ {name} остановлена" if ok else f"❌ Ошибка остановки {name}"
    )