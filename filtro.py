import re
import pandas as pd
import statistics


def process_terminal_output(output):
    pass_pattern = re.compile(r"\[PASS\] (\w+)\(.*?\) \(paths: \d+, time: ([\d.]+)s")
    fail_pattern = re.compile(r"\[FAIL\] (\w+)\(.*?\) \(paths: \d+, time: ([\d.]+)s")

    function_times = {}

    for line in output.splitlines():
        pass_match = pass_pattern.search(line)
        fail_match = fail_pattern.search(line)

        if pass_match:
            func_name, time = pass_match.groups()
            time = float(time)
            if func_name not in function_times:
                function_times[func_name] = {"status": "PASS", "times": []}
            function_times[func_name]["times"].append(time)
        elif fail_match:
            func_name, time = fail_match.groups()
            time = float(time)
            if func_name not in function_times:
                function_times[func_name] = {"status": "FAIL", "times": []}
            function_times[func_name]["times"].append(time)
            function_times[func_name]["status"] = "FAIL"

    rows = []
    max_num_times = max(len(data["times"]) for data in function_times.values())

    for func_name, data in function_times.items():
        times = data["times"]
        mean_time = round(statistics.mean(times), 2)
        std_time = round(statistics.stdev(times), 2) if len(times) > 1 else 0

        row = (
            [func_name, data["status"]]
            + times
            + [""] * (max_num_times - len(times))
            + [mean_time, std_time]
        )
        rows.append(row)

    columns = (
        ["Função", "Status"]
        + [f"Tempo {i+1}" for i in range(max_num_times)]
        + ["Média (s)", "Desvio Padrão (s)"]
    )

    df = pd.DataFrame(rows, columns=columns)

    total_tests = sum(len(data["times"]) for data in function_times.values())
    total_passed = sum(
        len(data["times"])
        for data in function_times.values()
        if data["status"] == "PASS"
    )

    markdown_table = "| " + " | ".join(df.columns) + " |\n"
    markdown_table += "| " + " | ".join(["---"] * len(df.columns)) + " |\n"
    for _, row in df.iterrows():
        markdown_table += (
            "| "
            + " | ".join([str(cell) if cell != "" else "-" for cell in row])
            + " |\n"
        )

    markdown_table += f"\n**Total de Testes Feitos:** {total_tests}\n"
    markdown_table += f"**Total de Testes Passados:** {total_passed}\n"

    return markdown_table


terminal_output = """
Counterexample: 
    p_id_uint256 = 0x0000000000000000000000000000000000000000000000000000000000000000 (0)
    p_initAmount_uint256 = 0x0000000000000000000000000000000000000000000000000000000000000000 (0)
[FAIL] proveFail_burnBalanceLessThanAmount(uint256,uint256,uint256) (paths: 1, time: 0.06s, bounds: [])
[PASS] proveFail_burnZeroAddress(uint256,uint256) (paths: 1, time: 0.01s, bounds: [])
[PASS] proveFail_mintZeroAddress(uint256,uint256) (paths: 1, time: 0.02s, bounds: [])
Counterexample: 
    p_id_uint256 = 0x0000000000000000000000000000000000000000000000000000000000000000 (0)
    p_initAmount_uint256 = 0x0000000000000000000000000000000000000000000000000000000000000000 (0)
[FAIL] proveFail_safeTransferFromBalanceLessThanAmount(uint256,uint256,uint256) (paths: 1, time: 0.05s, bounds: [])
[PASS] proveFail_safeTransferFromWhenSenderIsNotApprovedForAll(uint256,uint256) (paths: 2, time: 0.06s, bounds: [])
[PASS] proveFail_safeTransferFromWhenSenderIsNotMSGSender(uint256,uint256) (paths: 1, time: 0.02s, bounds: [])
[PASS] proveFail_safeTransferFromZeroAddressForFrom(uint256,uint256) (paths: 1, time: 0.02s, bounds: [])
[PASS] proveFail_safeTransferFromZeroAddressForTo(uint256,uint256) (paths: 1, time: 0.02s, bounds: [])
[PASS] proveFail_setApprovalForAllSenderEqualsOperator(address,bool) (paths: 4, time: 0.02s, bounds: [])
Counterexample: 
    p_amount_uint256 = 0x0000000000000000000000000000000000000000000000000000000000000000 (0)
    p_id_uint256 = 0x0000000000000000000000000000000000000000000000000000000000000000 (0)
[FAIL] prove_burn(uint256,uint256) (paths: 1, time: 0.04s, bounds: [])
Counterexample: 
    p_amount_uint256 = 0x0000000000000000000000000000000000000000000000000000000000000000 (0)
    p_id_uint256 = 0x0000000000000000000000000000000000000000000000000000000000000000 (0)
[FAIL] prove_mint(uint256,uint256) (paths: 1, time: 0.05s, bounds: [])
Counterexample: 
    p_ids[0]_uint256 = 0x0000000000000000000000000000000000000000000000000000000000000000 (0)
    p_ids[1]_uint256 = 0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff (115792089237316195423570985008687907853269984665640564039457584007913129639935)
    p_initAmount_uint256 = 0x0000000000000000000000000000000000000000000000000000000000000000 (0)
[FAIL] prove_safeBatchTransferFrom(uint256,uint256[],uint256[]) (paths: 2, time: 0.06s, bounds: [|ids|=2, |values|=2])
Counterexample: 
    p_id_uint256 = 0x0000000000000000000000000000000000000000000000000000000000000000 (0)
    p_initAmount_uint256 = 0x0000000000000000000000000000000000000000000000000000000000000000 (0)
[FAIL] prove_safeTransferFrom(uint256,uint256,uint256) (paths: 1, time: 0.04s, bounds: [])
[PASS] prove_setApprovalForAll(address,bool) (paths: 5, time: 0.03s, bounds: [])
Counterexample: 
    p_id_uint256 = 0x0000000000000000000000000000000000000000000000000000000000000000 (0)
    p_initAmount_uint256 = 0x0000000000000000000000000000000000000000000000000000000000000000 (0)
[FAIL] proveFail_burnBalanceLessThanAmount(uint256,uint256,uint256) (paths: 1, time: 0.07s, bounds: [])
[PASS] proveFail_burnZeroAddress(uint256,uint256) (paths: 1, time: 0.01s, bounds: [])
[PASS] proveFail_mintZeroAddress(uint256,uint256) (paths: 1, time: 0.02s, bounds: [])
Counterexample: 
    p_id_uint256 = 0x0000000000000000000000000000000000000000000000000000000000000000 (0)
    p_initAmount_uint256 = 0x0000000000000000000000000000000000000000000000000000000000000000 (0)
[FAIL] proveFail_safeTransferFromBalanceLessThanAmount(uint256,uint256,uint256) (paths: 1, time: 0.05s, bounds: [])
[PASS] proveFail_safeTransferFromWhenSenderIsNotApprovedForAll(uint256,uint256) (paths: 2, time: 0.07s, bounds: [])
[PASS] proveFail_safeTransferFromWhenSenderIsNotMSGSender(uint256,uint256) (paths: 1, time: 0.02s, bounds: [])
[PASS] proveFail_safeTransferFromZeroAddressForFrom(uint256,uint256) (paths: 1, time: 0.02s, bounds: [])
[PASS] proveFail_safeTransferFromZeroAddressForTo(uint256,uint256) (paths: 1, time: 0.02s, bounds: [])
[PASS] proveFail_setApprovalForAllSenderEqualsOperator(address,bool) (paths: 4, time: 0.02s, bounds: [])
Counterexample: 
    p_amount_uint256 = 0x0000000000000000000000000000000000000000000000000000000000000000 (0)
    p_id_uint256 = 0x0000000000000000000000000000000000000000000000000000000000000000 (0)
[FAIL] prove_burn(uint256,uint256) (paths: 1, time: 0.04s, bounds: [])
Counterexample: 
    p_amount_uint256 = 0x0000000000000000000000000000000000000000000000000000000000000000 (0)
    p_id_uint256 = 0x0000000000000000000000000000000000000000000000000000000000000000 (0)
[FAIL] prove_mint(uint256,uint256) (paths: 1, time: 0.05s, bounds: [])
Counterexample: 
    p_ids[0]_uint256 = 0x0000000000000000000000000000000000000000000000000000000000000000 (0)
    p_ids[1]_uint256 = 0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff (115792089237316195423570985008687907853269984665640564039457584007913129639935)
    p_initAmount_uint256 = 0x0000000000000000000000000000000000000000000000000000000000000000 (0)
[FAIL] prove_safeBatchTransferFrom(uint256,uint256[],uint256[]) (paths: 2, time: 0.06s, bounds: [|ids|=2, |values|=2])
Counterexample: 
    p_id_uint256 = 0x0000000000000000000000000000000000000000000000000000000000000000 (0)
    p_initAmount_uint256 = 0x0000000000000000000000000000000000000000000000000000000000000000 (0)
[FAIL] prove_safeTransferFrom(uint256,uint256,uint256) (paths: 1, time: 0.04s, bounds: [])
[PASS] prove_setApprovalForAll(address,bool) (paths: 5, time: 0.04s, bounds: [])
Counterexample: 
    p_id_uint256 = 0x0000000000000000000000000000000000000000000000000000000000000000 (0)
    p_initAmount_uint256 = 0x0000000000000000000000000000000000000000000000000000000000000000 (0)
[FAIL] proveFail_burnBalanceLessThanAmount(uint256,uint256,uint256) (paths: 1, time: 0.06s, bounds: [])
[PASS] proveFail_burnZeroAddress(uint256,uint256) (paths: 1, time: 0.01s, bounds: [])
[PASS] proveFail_mintZeroAddress(uint256,uint256) (paths: 1, time: 0.01s, bounds: [])
Counterexample: 
    p_id_uint256 = 0x0000000000000000000000000000000000000000000000000000000000000000 (0)
    p_initAmount_uint256 = 0x0000000000000000000000000000000000000000000000000000000000000000 (0)
[FAIL] proveFail_safeTransferFromBalanceLessThanAmount(uint256,uint256,uint256) (paths: 1, time: 0.05s, bounds: [])
[PASS] proveFail_safeTransferFromWhenSenderIsNotApprovedForAll(uint256,uint256) (paths: 2, time: 0.06s, bounds: [])
[PASS] proveFail_safeTransferFromWhenSenderIsNotMSGSender(uint256,uint256) (paths: 1, time: 0.02s, bounds: [])
[PASS] proveFail_safeTransferFromZeroAddressForFrom(uint256,uint256) (paths: 1, time: 0.02s, bounds: [])
[PASS] proveFail_safeTransferFromZeroAddressForTo(uint256,uint256) (paths: 1, time: 0.02s, bounds: [])
[PASS] proveFail_setApprovalForAllSenderEqualsOperator(address,bool) (paths: 4, time: 0.02s, bounds: [])
Counterexample: 
    p_amount_uint256 = 0x0000000000000000000000000000000000000000000000000000000000000000 (0)
    p_id_uint256 = 0x0000000000000000000000000000000000000000000000000000000000000000 (0)
[FAIL] prove_burn(uint256,uint256) (paths: 1, time: 0.04s, bounds: [])
Counterexample: 
    p_amount_uint256 = 0x0000000000000000000000000000000000000000000000000000000000000000 (0)
    p_id_uint256 = 0x0000000000000000000000000000000000000000000000000000000000000000 (0)
[FAIL] prove_mint(uint256,uint256) (paths: 1, time: 0.05s, bounds: [])
Counterexample: 
    p_ids[0]_uint256 = 0x0000000000000000000000000000000000000000000000000000000000000000 (0)
    p_ids[1]_uint256 = 0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff (115792089237316195423570985008687907853269984665640564039457584007913129639935)
    p_initAmount_uint256 = 0x0000000000000000000000000000000000000000000000000000000000000000 (0)
[FAIL] prove_safeBatchTransferFrom(uint256,uint256[],uint256[]) (paths: 2, time: 0.06s, bounds: [|ids|=2, |values|=2])
Counterexample: 
    p_id_uint256 = 0x0000000000000000000000000000000000000000000000000000000000000000 (0)
    p_initAmount_uint256 = 0x0000000000000000000000000000000000000000000000000000000000000000 (0)
[FAIL] prove_safeTransferFrom(uint256,uint256,uint256) (paths: 1, time: 0.04s, bounds: [])
[PASS] prove_setApprovalForAll(address,bool) (paths: 5, time: 0.03s, bounds: [])
Symbolic test result: 8 passed; 6 failed; time: 0.75s

Running 1 tests for src/openzeppelin-contracts/lib/forge-std/lib/ds-test/demo/demo.sol:DemoTest
[PASS] prove_this(uint256) (paths: 2, time: 0.04s, bounds: [])
Counterexample: 
    p_id_uint256 = 0x0000000000000000000000000000000000000000000000000000000000000000 (0)
    p_initAmount_uint256 = 0x0000000000000000000000000000000000000000000000000000000000000000 (0)
[FAIL] proveFail_burnBalanceLessThanAmount(uint256,uint256,uint256) (paths: 1, time: 0.06s, bounds: [])
[PASS] proveFail_burnZeroAddress(uint256,uint256) (paths: 1, time: 0.01s, bounds: [])
[PASS] proveFail_mintZeroAddress(uint256,uint256) (paths: 1, time: 0.01s, bounds: [])
Counterexample: 
    p_id_uint256 = 0x0000000000000000000000000000000000000000000000000000000000000000 (0)
    p_initAmount_uint256 = 0x0000000000000000000000000000000000000000000000000000000000000000 (0)
[FAIL] proveFail_safeTransferFromBalanceLessThanAmount(uint256,uint256,uint256) (paths: 1, time: 0.05s, bounds: [])
[PASS] proveFail_safeTransferFromWhenSenderIsNotApprovedForAll(uint256,uint256) (paths: 2, time: 0.06s, bounds: [])
[PASS] proveFail_safeTransferFromWhenSenderIsNotMSGSender(uint256,uint256) (paths: 1, time: 0.02s, bounds: [])
[PASS] proveFail_safeTransferFromZeroAddressForFrom(uint256,uint256) (paths: 1, time: 0.02s, bounds: [])
[PASS] proveFail_safeTransferFromZeroAddressForTo(uint256,uint256) (paths: 1, time: 0.02s, bounds: [])
[PASS] proveFail_setApprovalForAllSenderEqualsOperator(address,bool) (paths: 4, time: 0.02s, bounds: [])
Counterexample: 
    p_amount_uint256 = 0x0000000000000000000000000000000000000000000000000000000000000000 (0)
    p_id_uint256 = 0x0000000000000000000000000000000000000000000000000000000000000000 (0)
[FAIL] prove_burn(uint256,uint256) (paths: 1, time: 0.04s, bounds: [])
Counterexample: 
    p_amount_uint256 = 0x0000000000000000000000000000000000000000000000000000000000000000 (0)
    p_id_uint256 = 0x0000000000000000000000000000000000000000000000000000000000000000 (0)
[FAIL] prove_mint(uint256,uint256) (paths: 1, time: 0.05s, bounds: [])
Counterexample: 
    p_ids[0]_uint256 = 0x0000000000000000000000000000000000000000000000000000000000000000 (0)
    p_ids[1]_uint256 = 0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff (115792089237316195423570985008687907853269984665640564039457584007913129639935)
    p_initAmount_uint256 = 0x0000000000000000000000000000000000000000000000000000000000000000 (0)
[FAIL] prove_safeBatchTransferFrom(uint256,uint256[],uint256[]) (paths: 2, time: 0.06s, bounds: [|ids|=2, |values|=2])
Counterexample: 
    p_id_uint256 = 0x0000000000000000000000000000000000000000000000000000000000000000 (0)
    p_initAmount_uint256 = 0x0000000000000000000000000000000000000000000000000000000000000000 (0)
[FAIL] prove_safeTransferFrom(uint256,uint256,uint256) (paths: 1, time: 0.04s, bounds: [])
[PASS] prove_setApprovalForAll(address,bool) (paths: 5, time: 0.03s, bounds: [])
Counterexample: 
    p_id_uint256 = 0x0000000000000000000000000000000000000000000000000000000000000000 (0)
    p_initAmount_uint256 = 0x0000000000000000000000000000000000000000000000000000000000000000 (0)
[FAIL] proveFail_burnBalanceLessThanAmount(uint256,uint256,uint256) (paths: 1, time: 0.06s, bounds: [])
[PASS] proveFail_burnZeroAddress(uint256,uint256) (paths: 1, time: 0.01s, bounds: [])
[PASS] proveFail_mintZeroAddress(uint256,uint256) (paths: 1, time: 0.02s, bounds: [])
Counterexample: 
    p_id_uint256 = 0x0000000000000000000000000000000000000000000000000000000000000000 (0)
    p_initAmount_uint256 = 0x0000000000000000000000000000000000000000000000000000000000000000 (0)
[FAIL] proveFail_safeTransferFromBalanceLessThanAmount(uint256,uint256,uint256) (paths: 1, time: 0.05s, bounds: [])
[PASS] proveFail_safeTransferFromWhenSenderIsNotApprovedForAll(uint256,uint256) (paths: 2, time: 0.07s, bounds: [])
[PASS] proveFail_safeTransferFromWhenSenderIsNotMSGSender(uint256,uint256) (paths: 1, time: 0.02s, bounds: [])
[PASS] proveFail_safeTransferFromZeroAddressForFrom(uint256,uint256) (paths: 1, time: 0.02s, bounds: [])
[PASS] proveFail_safeTransferFromZeroAddressForTo(uint256,uint256) (paths: 1, time: 0.02s, bounds: [])
[PASS] proveFail_setApprovalForAllSenderEqualsOperator(address,bool) (paths: 4, time: 0.02s, bounds: [])
Counterexample: 
    p_amount_uint256 = 0x0000000000000000000000000000000000000000000000000000000000000000 (0)
    p_id_uint256 = 0x0000000000000000000000000000000000000000000000000000000000000000 (0)
[FAIL] prove_burn(uint256,uint256) (paths: 1, time: 0.04s, bounds: [])
Counterexample: 
    p_amount_uint256 = 0x0000000000000000000000000000000000000000000000000000000000000000 (0)
    p_id_uint256 = 0x0000000000000000000000000000000000000000000000000000000000000000 (0)
[FAIL] prove_mint(uint256,uint256) (paths: 1, time: 0.05s, bounds: [])
Counterexample: 
    p_ids[0]_uint256 = 0x0000000000000000000000000000000000000000000000000000000000000000 (0)
    p_ids[1]_uint256 = 0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff (115792089237316195423570985008687907853269984665640564039457584007913129639935)
    p_initAmount_uint256 = 0x0000000000000000000000000000000000000000000000000000000000000000 (0)
[FAIL] prove_safeBatchTransferFrom(uint256,uint256[],uint256[]) (paths: 2, time: 0.06s, bounds: [|ids|=2, |values|=2])
Counterexample: 
    p_id_uint256 = 0x0000000000000000000000000000000000000000000000000000000000000000 (0)
    p_initAmount_uint256 = 0x0000000000000000000000000000000000000000000000000000000000000000 (0)
[FAIL] prove_safeTransferFrom(uint256,uint256,uint256) (paths: 1, time: 0.04s, bounds: [])
[PASS] prove_setApprovalForAll(address,bool) (paths: 5, time: 0.03s, bounds: [])
Counterexample: 
    p_id_uint256 = 0x0000000000000000000000000000000000000000000000000000000000000000 (0)
    p_initAmount_uint256 = 0x0000000000000000000000000000000000000000000000000000000000000000 (0)
[FAIL] proveFail_burnBalanceLessThanAmount(uint256,uint256,uint256) (paths: 1, time: 0.06s, bounds: [])
[PASS] proveFail_burnZeroAddress(uint256,uint256) (paths: 1, time: 0.01s, bounds: [])
[PASS] proveFail_mintZeroAddress(uint256,uint256) (paths: 1, time: 0.02s, bounds: [])
Counterexample: 
    p_id_uint256 = 0x0000000000000000000000000000000000000000000000000000000000000000 (0)
    p_initAmount_uint256 = 0x0000000000000000000000000000000000000000000000000000000000000000 (0)
[FAIL] proveFail_safeTransferFromBalanceLessThanAmount(uint256,uint256,uint256) (paths: 1, time: 0.05s, bounds: [])
[PASS] proveFail_safeTransferFromWhenSenderIsNotApprovedForAll(uint256,uint256) (paths: 2, time: 0.06s, bounds: [])
[PASS] proveFail_safeTransferFromWhenSenderIsNotMSGSender(uint256,uint256) (paths: 1, time: 0.02s, bounds: [])
[PASS] proveFail_safeTransferFromZeroAddressForFrom(uint256,uint256) (paths: 1, time: 0.02s, bounds: [])
[PASS] proveFail_safeTransferFromZeroAddressForTo(uint256,uint256) (paths: 1, time: 0.02s, bounds: [])
[PASS] proveFail_setApprovalForAllSenderEqualsOperator(address,bool) (paths: 4, time: 0.02s, bounds: [])
Counterexample: 
    p_amount_uint256 = 0x0000000000000000000000000000000000000000000000000000000000000000 (0)
    p_id_uint256 = 0x0000000000000000000000000000000000000000000000000000000000000000 (0)
[FAIL] prove_burn(uint256,uint256) (paths: 1, time: 0.04s, bounds: [])
Counterexample: 
    p_amount_uint256 = 0x0000000000000000000000000000000000000000000000000000000000000000 (0)
    p_id_uint256 = 0x0000000000000000000000000000000000000000000000000000000000000000 (0)
[FAIL] prove_mint(uint256,uint256) (paths: 1, time: 0.05s, bounds: [])
Counterexample: 
    p_ids[0]_uint256 = 0x0000000000000000000000000000000000000000000000000000000000000000 (0)
    p_ids[1]_uint256 = 0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff (115792089237316195423570985008687907853269984665640564039457584007913129639935)
    p_initAmount_uint256 = 0x0000000000000000000000000000000000000000000000000000000000000000 (0)
[FAIL] prove_safeBatchTransferFrom(uint256,uint256[],uint256[]) (paths: 2, time: 0.06s, bounds: [|ids|=2, |values|=2])
Counterexample: 
    p_id_uint256 = 0x0000000000000000000000000000000000000000000000000000000000000000 (0)
    p_initAmount_uint256 = 0x0000000000000000000000000000000000000000000000000000000000000000 (0)
[FAIL] prove_safeTransferFrom(uint256,uint256,uint256) (paths: 1, time: 0.04s, bounds: [])
[PASS] prove_setApprovalForAll(address,bool) (paths: 5, time: 0.04s, bounds: [])
Counterexample: 
    p_id_uint256 = 0x0000000000000000000000000000000000000000000000000000000000000000 (0)
    p_initAmount_uint256 = 0x0000000000000000000000000000000000000000000000000000000000000000 (0)
[FAIL] proveFail_burnBalanceLessThanAmount(uint256,uint256,uint256) (paths: 1, time: 0.06s, bounds: [])
[PASS] proveFail_burnZeroAddress(uint256,uint256) (paths: 1, time: 0.01s, bounds: [])
[PASS] proveFail_mintZeroAddress(uint256,uint256) (paths: 1, time: 0.02s, bounds: [])
Counterexample: 
    p_id_uint256 = 0x0000000000000000000000000000000000000000000000000000000000000000 (0)
    p_initAmount_uint256 = 0x0000000000000000000000000000000000000000000000000000000000000000 (0)
[FAIL] proveFail_safeTransferFromBalanceLessThanAmount(uint256,uint256,uint256) (paths: 1, time: 0.05s, bounds: [])
[PASS] proveFail_safeTransferFromWhenSenderIsNotApprovedForAll(uint256,uint256) (paths: 2, time: 0.07s, bounds: [])
[PASS] proveFail_safeTransferFromWhenSenderIsNotMSGSender(uint256,uint256) (paths: 1, time: 0.02s, bounds: [])
[PASS] proveFail_safeTransferFromZeroAddressForFrom(uint256,uint256) (paths: 1, time: 0.02s, bounds: [])
[PASS] proveFail_safeTransferFromZeroAddressForTo(uint256,uint256) (paths: 1, time: 0.02s, bounds: [])
[PASS] proveFail_setApprovalForAllSenderEqualsOperator(address,bool) (paths: 4, time: 0.02s, bounds: [])
Counterexample: 
    p_amount_uint256 = 0x0000000000000000000000000000000000000000000000000000000000000000 (0)
    p_id_uint256 = 0x0000000000000000000000000000000000000000000000000000000000000000 (0)
[FAIL] prove_burn(uint256,uint256) (paths: 1, time: 0.04s, bounds: [])
Counterexample: 
    p_amount_uint256 = 0x0000000000000000000000000000000000000000000000000000000000000000 (0)
    p_id_uint256 = 0x0000000000000000000000000000000000000000000000000000000000000000 (0)
[FAIL] prove_mint(uint256,uint256) (paths: 1, time: 0.05s, bounds: [])
Counterexample: 
    p_ids[0]_uint256 = 0x0000000000000000000000000000000000000000000000000000000000000000 (0)
    p_ids[1]_uint256 = 0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff (115792089237316195423570985008687907853269984665640564039457584007913129639935)
    p_initAmount_uint256 = 0x0000000000000000000000000000000000000000000000000000000000000000 (0)
[FAIL] prove_safeBatchTransferFrom(uint256,uint256[],uint256[]) (paths: 2, time: 0.07s, bounds: [|ids|=2, |values|=2])
Counterexample: 
    p_id_uint256 = 0x0000000000000000000000000000000000000000000000000000000000000000 (0)
    p_initAmount_uint256 = 0x0000000000000000000000000000000000000000000000000000000000000000 (0)
[FAIL] prove_safeTransferFrom(uint256,uint256,uint256) (paths: 1, time: 0.05s, bounds: [])
[PASS] prove_setApprovalForAll(address,bool) (paths: 5, time: 0.04s, bounds: [])
Counterexample: 
    p_id_uint256 = 0x0000000000000000000000000000000000000000000000000000000000000000 (0)
    p_initAmount_uint256 = 0x0000000000000000000000000000000000000000000000000000000000000000 (0)
[FAIL] proveFail_burnBalanceLessThanAmount(uint256,uint256,uint256) (paths: 1, time: 0.06s, bounds: [])
[PASS] proveFail_burnZeroAddress(uint256,uint256) (paths: 1, time: 0.01s, bounds: [])
[PASS] proveFail_mintZeroAddress(uint256,uint256) (paths: 1, time: 0.01s, bounds: [])
Counterexample: 
    p_id_uint256 = 0x0000000000000000000000000000000000000000000000000000000000000000 (0)
    p_initAmount_uint256 = 0x0000000000000000000000000000000000000000000000000000000000000000 (0)
[FAIL] proveFail_safeTransferFromBalanceLessThanAmount(uint256,uint256,uint256) (paths: 1, time: 0.05s, bounds: [])
[PASS] proveFail_safeTransferFromWhenSenderIsNotApprovedForAll(uint256,uint256) (paths: 2, time: 0.06s, bounds: [])
[PASS] proveFail_safeTransferFromWhenSenderIsNotMSGSender(uint256,uint256) (paths: 1, time: 0.02s, bounds: [])
[PASS] proveFail_safeTransferFromZeroAddressForFrom(uint256,uint256) (paths: 1, time: 0.02s, bounds: [])
[PASS] proveFail_safeTransferFromZeroAddressForTo(uint256,uint256) (paths: 1, time: 0.02s, bounds: [])
[PASS] proveFail_setApprovalForAllSenderEqualsOperator(address,bool) (paths: 4, time: 0.02s, bounds: [])
Counterexample: 
    p_amount_uint256 = 0x0000000000000000000000000000000000000000000000000000000000000000 (0)
    p_id_uint256 = 0x0000000000000000000000000000000000000000000000000000000000000000 (0)
[FAIL] prove_burn(uint256,uint256) (paths: 1, time: 0.04s, bounds: [])
Counterexample: 
    p_amount_uint256 = 0x0000000000000000000000000000000000000000000000000000000000000000 (0)
    p_id_uint256 = 0x0000000000000000000000000000000000000000000000000000000000000000 (0)
[FAIL] prove_mint(uint256,uint256) (paths: 1, time: 0.05s, bounds: [])
Counterexample: 
    p_ids[0]_uint256 = 0x0000000000000000000000000000000000000000000000000000000000000000 (0)
    p_ids[1]_uint256 = 0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff (115792089237316195423570985008687907853269984665640564039457584007913129639935)
    p_initAmount_uint256 = 0x0000000000000000000000000000000000000000000000000000000000000000 (0)
[FAIL] prove_safeBatchTransferFrom(uint256,uint256[],uint256[]) (paths: 2, time: 0.06s, bounds: [|ids|=2, |values|=2])
Counterexample: 
    p_id_uint256 = 0x0000000000000000000000000000000000000000000000000000000000000000 (0)
    p_initAmount_uint256 = 0x0000000000000000000000000000000000000000000000000000000000000000 (0)
[FAIL] prove_safeTransferFrom(uint256,uint256,uint256) (paths: 1, time: 0.04s, bounds: [])
[PASS] prove_setApprovalForAll(address,bool) (paths: 5, time: 0.03s, bounds: [])
Counterexample: 
    p_id_uint256 = 0x0000000000000000000000000000000000000000000000000000000000000000 (0)
    p_initAmount_uint256 = 0x0000000000000000000000000000000000000000000000000000000000000000 (0)
[FAIL] proveFail_burnBalanceLessThanAmount(uint256,uint256,uint256) (paths: 1, time: 0.06s, bounds: [])
[PASS] proveFail_burnZeroAddress(uint256,uint256) (paths: 1, time: 0.01s, bounds: [])
[PASS] proveFail_mintZeroAddress(uint256,uint256) (paths: 1, time: 0.02s, bounds: [])
Counterexample: 
    p_id_uint256 = 0x0000000000000000000000000000000000000000000000000000000000000000 (0)
    p_initAmount_uint256 = 0x0000000000000000000000000000000000000000000000000000000000000000 (0)
[FAIL] proveFail_safeTransferFromBalanceLessThanAmount(uint256,uint256,uint256) (paths: 1, time: 0.05s, bounds: [])
[PASS] proveFail_safeTransferFromWhenSenderIsNotApprovedForAll(uint256,uint256) (paths: 2, time: 0.07s, bounds: [])
[PASS] proveFail_safeTransferFromWhenSenderIsNotMSGSender(uint256,uint256) (paths: 1, time: 0.02s, bounds: [])
[PASS] proveFail_safeTransferFromZeroAddressForFrom(uint256,uint256) (paths: 1, time: 0.02s, bounds: [])
[PASS] proveFail_safeTransferFromZeroAddressForTo(uint256,uint256) (paths: 1, time: 0.02s, bounds: [])
[PASS] proveFail_setApprovalForAllSenderEqualsOperator(address,bool) (paths: 4, time: 0.02s, bounds: [])
Counterexample: 
    p_amount_uint256 = 0x0000000000000000000000000000000000000000000000000000000000000000 (0)
    p_id_uint256 = 0x0000000000000000000000000000000000000000000000000000000000000000 (0)
[FAIL] prove_burn(uint256,uint256) (paths: 1, time: 0.04s, bounds: [])
Counterexample: 
    p_amount_uint256 = 0x0000000000000000000000000000000000000000000000000000000000000000 (0)
    p_id_uint256 = 0x0000000000000000000000000000000000000000000000000000000000000000 (0)
[FAIL] prove_mint(uint256,uint256) (paths: 1, time: 0.05s, bounds: [])
Counterexample: 
    p_ids[0]_uint256 = 0x0000000000000000000000000000000000000000000000000000000000000000 (0)
    p_ids[1]_uint256 = 0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff (115792089237316195423570985008687907853269984665640564039457584007913129639935)
    p_initAmount_uint256 = 0x0000000000000000000000000000000000000000000000000000000000000000 (0)
[FAIL] prove_safeBatchTransferFrom(uint256,uint256[],uint256[]) (paths: 2, time: 0.06s, bounds: [|ids|=2, |values|=2])
Counterexample: 
    p_id_uint256 = 0x0000000000000000000000000000000000000000000000000000000000000000 (0)
    p_initAmount_uint256 = 0x0000000000000000000000000000000000000000000000000000000000000000 (0)
[FAIL] prove_safeTransferFrom(uint256,uint256,uint256) (paths: 1, time: 0.04s, bounds: [])
[PASS] prove_setApprovalForAll(address,bool) (paths: 5, time: 0.03s, bounds: [])
Counterexample: 
    p_id_uint256 = 0x0000000000000000000000000000000000000000000000000000000000000000 (0)
    p_initAmount_uint256 = 0x0000000000000000000000000000000000000000000000000000000000000000 (0)
[FAIL] proveFail_burnBalanceLessThanAmount(uint256,uint256,uint256) (paths: 1, time: 0.06s, bounds: [])
[PASS] proveFail_burnZeroAddress(uint256,uint256) (paths: 1, time: 0.01s, bounds: [])
[PASS] proveFail_mintZeroAddress(uint256,uint256) (paths: 1, time: 0.02s, bounds: [])
Counterexample: 
    p_id_uint256 = 0x0000000000000000000000000000000000000000000000000000000000000000 (0)
    p_initAmount_uint256 = 0x0000000000000000000000000000000000000000000000000000000000000000 (0)
[FAIL] proveFail_safeTransferFromBalanceLessThanAmount(uint256,uint256,uint256) (paths: 1, time: 0.05s, bounds: [])
[PASS] proveFail_safeTransferFromWhenSenderIsNotApprovedForAll(uint256,uint256) (paths: 2, time: 0.06s, bounds: [])
[PASS] proveFail_safeTransferFromWhenSenderIsNotMSGSender(uint256,uint256) (paths: 1, time: 0.02s, bounds: [])
[PASS] proveFail_safeTransferFromZeroAddressForFrom(uint256,uint256) (paths: 1, time: 0.02s, bounds: [])
[PASS] proveFail_safeTransferFromZeroAddressForTo(uint256,uint256) (paths: 1, time: 0.02s, bounds: [])
[PASS] proveFail_setApprovalForAllSenderEqualsOperator(address,bool) (paths: 4, time: 0.02s, bounds: [])
Counterexample: 
    p_amount_uint256 = 0x0000000000000000000000000000000000000000000000000000000000000000 (0)
    p_id_uint256 = 0x0000000000000000000000000000000000000000000000000000000000000000 (0)
[FAIL] prove_burn(uint256,uint256) (paths: 1, time: 0.04s, bounds: [])
Counterexample: 
    p_amount_uint256 = 0x0000000000000000000000000000000000000000000000000000000000000000 (0)
    p_id_uint256 = 0x0000000000000000000000000000000000000000000000000000000000000000 (0)
[FAIL] prove_mint(uint256,uint256) (paths: 1, time: 0.05s, bounds: [])
Counterexample: 
    p_ids[0]_uint256 = 0x0000000000000000000000000000000000000000000000000000000000000000 (0)
    p_ids[1]_uint256 = 0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff (115792089237316195423570985008687907853269984665640564039457584007913129639935)
    p_initAmount_uint256 = 0x0000000000000000000000000000000000000000000000000000000000000000 (0)
[FAIL] prove_safeBatchTransferFrom(uint256,uint256[],uint256[]) (paths: 2, time: 0.06s, bounds: [|ids|=2, |values|=2])
Counterexample: 
    p_id_uint256 = 0x0000000000000000000000000000000000000000000000000000000000000000 (0)
    p_initAmount_uint256 = 0x0000000000000000000000000000000000000000000000000000000000000000 (0)
[FAIL] prove_safeTransferFrom(uint256,uint256,uint256) (paths: 1, time: 0.04s, bounds: [])
[PASS] prove_setApprovalForAll(address,bool) (paths: 5, time: 0.03s, bounds: [])
"""

markdown_result = process_terminal_output(terminal_output)
print(markdown_result)
