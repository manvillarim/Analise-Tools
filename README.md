# DESEMPENHO DO HALMOS NOS TESTES SIMBÓLICOS DO ERC20(OPPEN ZEPPELIN)

 **DESEMPENHO DE CADA TESTE ESPECÍFICO**


| Função | Status | Tempo 1 | Tempo 2 | Tempo 3 | Tempo 4 | Tempo 5 | Tempo 6 | Tempo 7 | Tempo 8 | Tempo 9 | Tempo 10 | Média (s) | Desvio Padrão (s) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| proveFail_ApproveFromZeroAddress | PASS | 0.03 | 0.03 | 0.03 | 0.03 | 0.03 | 0.03 | 0.03 | 0.02 | 0.03 | 0.02 | 0.03 | 0.0 |
| proveFail_ApproveToZeroAddress | PASS | 0.02 | 0.02 | 0.02 | 0.02 | 0.02 | 0.02 | 0.02 | 0.02 | 0.02 | 0.02 | 0.02 | 0.0 |
| proveFail_ApproveZeroAddress | ERROR | 0.02 | 0.02 | 0.02 | 0.02 | 0.02 | 0.02 | 0.02 | 0.02 | 0.02 | 0.02| 0.02 | 0.0 |
| proveFail_ApproveZeroAddressForMSGSender | ERROR | 0.01 | 0.01 | 0.01 | 0.01 | 0.01 | 0.01 | 0.01 | 0.01 | 0.01 | 0.01 | 0.01 | 0.0 |
| proveFail_BurnFromZeroAddress | PASS | 0.01 | 0.01 | 0.01 | 0.01 | 0.01 | 0.01 | 0.02 | 0.01 | 0.01 | 0.01 | 0.01 | 0.0 |
| proveFail_BurnUnderBalance | PASS | 0.04 | 0.04 | 0.04 | 0.04 | 0.04 | 0.04 | 0.04 | 0.04 | 0.03 | 0.04 | 0.04 | 0.0 |
| proveFail_BurnUnderSupply | ERROR | 0.03 | 0.03 | 0.03 | 0.03 | 0.04 | 0.03 | 0.03 | 0.03 | 0.03 | 0.03 | 0.03 | 0.0 |
| proveFail_DecreaseAllowanceUnderAllowance | ERROR | 0.03 | 0.03 | 0.03 | 0.03 | 0.03 | 0.03 | 0.03 | 0.03 | 0.03 | 0.03| 0.03 | 0.0 |
| proveFail_IncreaseAllowanceUnderAllowance | ERROR | 0.02 | 0.02 | 0.02 | 0.02 | 0.02 | 0.02 | 0.02 | 0.02 | 0.02 | 0.02| 0.02 | 0.0 |
| proveFail_MintOverflow | PASS | 0.03 | 0.03 | 0.03 | 0.03 | 0.03 | 0.03 | 0.03 | 0.03 | 0.03 | 0.03| 0.03 | 0.0 |
| proveFail_MintToZeroAddress | PASS | 0.01 | 0.01 | 0.01 | 0.01 | 0.01 | 0.01 | 0.01 | 0.01 | 0.01 | 0.01 | 0.01 | 0.0 |
| proveFail_MintUnderSupply | ERROR | 0.02 | 0.02 | 0.02 | 0.03 | 0.03 | 0.02 | 0.02 | 0.03 | 0.02 | 0.02| 0.02 | 0.0 |
| proveFail_TransferFromNotEnoughAmount | ERROR | 0.05 | 0.05 | 0.04 | 0.05 | 0.05 | 0.05 | 0.04 | 0.04 | 0.05 | 0.05| 0.05 | 0.0 |
| proveFail_TransferFromToZeroAddress | PASS | 0.08 | 0.08 | 0.08 | 0.08 | 0.08 | 0.08 | 0.08 | 0.08 | 0.08 | 0.09| 0.08 | 0.0 |
| proveFail_TransferFromUnderBalance | PASS | 0.18 | 0.18 | 0.18 | 0.18 | 0.18 | 0.18 | 0.18 | 0.18 | 0.18 | 0.19| 0.18 | 0.0 |
| proveFail_TransferFromUnderBalancei | ERROR | 0.05 | 0.06 | 0.05 | 0.05 | 0.05 | 0.05 | 0.05 | 0.05 | 0.05 | 0.06| 0.05 | 0.0 |
| proveFail_TransferFromZeroAddress | PASS | 0.03 | 0.02 | 0.03 | 0.02 | 0.03 | 0.02 | 0.03 | 0.02 | 0.03 | 0.02 | 0.03 | 0.01 |
| proveFail_TransferFromZeroAddressForMSGSender | ERROR | 0.01 | 0.01 | 0.01 | 0.01 | 0.01 | 0.01 | 0.01 | 0.01 | 0.01 | 0.01| 0.01 | 0.0 |
| proveFail_TransferToZeroAddress | PASS | 0.04 | 0.04 | 0.04 | 0.04 | 0.04 | 0.04 | 0.04 | 0.04 | 0.04 | 0.04| 0.04 | 0.0 |
| proveFail_TransferUnderBalance | PASS | 0.09 | 0.09 | 0.09 | 0.09 | 0.09 | 0.08 | 0.09 | 0.08 | 0.09 | 0.09| 0.09 | 0.0 |
| proveFail_TransferUnderBalancej | ERROR | 0.03 | 0.03 | 0.03 | 0.03 | 0.03 | 0.03 | 0.04 | 0.03 | 0.03 | 0.03| 0.03 | 0.0 |
| prove_AllowanceUpdatedAfterBurn | PASS | 0.07 | 0.07 | 0.07 | 0.07 | 0.07 | 0.07 | 0.08 | 0.07 | 0.07 | 0.08| 0.07 | 0.0 |
| prove_Approve | PASS | 0.03 | 0.03 | 0.03 | 0.03 | 0.03 | 0.03 | 0.03 | 0.03 | 0.03 | 0.03| 0.03 | 0.0 |
| prove_ApproveMaxAmount | PASS | 0.04 | 0.04 | 0.04 | 0.04 | 0.04 | 0.04 | 0.04 | 0.04 | 0.04 | 0.04| 0.04 | 0.0 |
| prove_ApproveNonZeroAmount | PASS | 0.04 | 0.04 | 0.04 | 0.04 | 0.04 | 0.05 | 0.04 | 0.04 | 0.04 | 0.04| 0.04 | 0.0 |
| prove_ApproveZeroAmount | PASS | 0.04 | 0.04 | 0.04 | 0.04 | 0.04 | 0.04 | 0.04 | 0.04 | 0.04 | 0.04| 0.04 | 0.0 |
| prove_BalanceUpdatedAfterBurn | PASS | 0.1 | 0.1 | 0.1 | 0.09 | 0.1 | 0.1 | 0.1 | 0.09 | 0.1 | 0.1| 0.1 | 0.0 |
| prove_BurnDifferentAccount | PASS | 0.12 | 0.12 | 0.12 | 0.12 | 0.12 | 0.12 | 0.12 | 0.12 | 0.13 | 0.13| 0.12 | 0.0 |
| prove_BurnFromNonZeroAddress | PASS | 0.05 | 0.05 | 0.05 | 0.05 | 0.05 | 0.05 | 0.05 | 0.05 | 0.06 | 0.06| 0.05 | 0.0 |
| prove_BurnSameAccount | PASS | 0.06 | 0.06 | 0.06 | 0.06 | 0.06 | 0.06 | 0.07 | 0.06 | 0.06 | 0.06| 0.06 | 0.0 |
| prove_BurnZeroTokens | PASS | 0.04 | 0.04 | 0.04 | 0.03 | 0.04 | 0.04 | 0.04 | 0.04 | 0.03 | 0.04| 0.04 | 0.0 |
| prove_ConsecutiveApprovePositiveToPositive | PASS | 0.06 | 0.06 | 0.06 | 0.06 | 0.06 | 0.06 | 0.06 | 0.06 | 0.06 | 0.06| 0.06 | 0.0 |
| prove_DecreaseAllowance | PASS | 0.08 | 0.08 | 0.08 | 0.08 | 0.08 | 0.08 | 0.09 | 0.08 | 0.08 | 0.09| 0.08 | 0.0 |
| prove_IncreaseAllowance | PASS | 0.07 | 0.07 | 0.07 | 0.07 | 0.08 | 0.07 | 0.08 | 0.07 | 0.07 | 0.08| 0.07 | 0.0 |
| prove_Mint | PASS | 0.05 | 0.05 | 0.05 | 0.05 | 0.05 | 0.05 | 0.05 | 0.05 | 0.05 | 0.05| 0.05 | 0.0 |
| prove_MintZeroTokens | PASS | 0.03 | 0.04 | 0.03 | 0.03 | 0.04 | 0.03 | 0.04 | 0.03 | 0.03 | 0.03| 0.03 | 0.0 |
| prove_MsgSenderCanRetrieveOtherBalance | PASS | 0.03 | 0.03 | 0.03 | 0.03 | 0.04 | 0.03 | 0.03 | 0.03 | 0.03 | 0.03| 0.03 | 0.0 |
| prove_MsgSenderCanRetrieveOwnBalance | PASS | 0.02 | 0.02 | 0.02 | 0.02 | 0.02 | 0.02 | 0.02 | 0.02 | 0.02 | 0.02| 0.02 | 0.0 |
| prove_MsgSenderCanTransferTotalBalance | PASS | 0.09 | 0.09 | 0.09 | 0.09 | 0.09 | 0.09 | 0.09 | 0.09 | 0.09 | 0.09| 0.09 | 0.0 |
| prove_MsgSenderCanTransferTotalBalanceZero | PASS | 0.07 | 0.07 | 0.07 | 0.07 | 0.08 | 0.07 | 0.07 | 0.07 | 0.07 | 0.07| 0.07 | 0.0 |
| prove_MultipleTransferFromAllowed | PASS | 0.31 | 0.31 | 0.31 | 0.31 | 0.35 | 0.31 | 0.31 | 0.33 | 0.3 | 0.31| 0.32 | 0.01 |
| prove_MultipleTransferFromsOfZeroAmountAllowed | PASS | 0.19 | 0.21 | 0.19 | 0.18 | 0.21 | 0.19 | 0.19 | 0.2 | 0.18 | 0.18| 0.19 | 0.01 |
| prove_MultipleTransfersAllowed | PASS | 0.13 | 0.13 | 0.13 | 0.13 | 0.15 | 0.13 | 0.13 | 0.14 | 0.12 | 0.13| 0.13 | 0.01 |
| prove_MultipleTransfersOfZeroAmountAllowed | PASS | 0.16 | 0.14 | 0.17 | 0.17 | 0.18 | 0.17 | 0.17 | 0.17 | 0.16 | 0.17| 0.17 | 0.01 |
| prove_SelfApproveAndTransferFromOwnAccount | PASS | 0.17 | 0.17 | 0.17 | 0.17 | 0.18 | 0.17 | 0.17 | 0.18 | 0.17 | 0.17| 0.17 | 0.0 |
| prove_SelfApproveAndTransferFromOwnAccountZeroAmountAllowed | PASS | 0.11 | 0.1 | 0.1 | 0.11 | 0.1 | 0.13 | 0.09 | 0.09 | 0.09 | 0.09| 0.1 | 0.01 |
| prove_SelfApprovePositiveAmount | PASS | 0.04 | 0.04 | 0.04 | 0.04 | 0.04 | 0.04 | 0.04 | 0.04 | 0.04 | 0.04| 0.04 | 0.0 |
| prove_SelfApproveZeroAmountAllowed | PASS | 0.03 | 0.03 | 0.03 | 0.03 | 0.03 | 0.03 | 0.03 | 0.03 | 0.03 | 0.04| 0.03 | 0.0 |
| prove_SelfTransferPositiveAmountAllowed | PASS | 0.06 | 0.06 | 0.06 | 0.06 | 0.06 | 0.06 | 0.06 | 0.06 | 0.06 | 0.06| 0.06 | 0.0 |
| prove_SelfTransferZeroAmountAllowed | PASS | 0.04 | 0.04 | 0.04 | 0.04 | 0.04 | 0.04 | 0.04 | 0.04 | 0.04 | 0.04| 0.04 | 0.0 |
| prove_TokenReceiverCanTransferFromTotalBalance | PASS | 0.17 | 0.17 | 0.17 | 0.17 | 0.2 | 0.17 | 0.17 | 0.18 | 0.16 | 0.17| 0.17 | 0.01 |
| prove_TokenReceiverCanTransferFromTotalBalanceZero | PASS | 0.14 | 0.11 | 0.11 | 0.11 | 0.12 | 0.12 | 0.14 | 0.12 | 0.11 | 0.11| 0.12 | 0.01 |
| prove_Transfer | PASS | 0.1 | 0.1 | 0.1 | 0.1 | 0.12 | 0.1 | 0.1 | 0.11 | 0.1 | 0.1| 0.1 | 0.01 |
| prove_TransferDoesNotUpdateOtherBalances | PASS | 0.14 | 0.14 | 0.14 | 0.14 | 0.16 | 0.14 | 0.14 | 0.17 | 0.13 | 0.14| 0.14 | 0.01 |
| prove_TransferFrom | PASS | 0.17 | 0.16 | 0.16 | 0.16 | 0.18 | 0.16 | 0.16 | 0.18 | 0.16 | 0.16| 0.17 | 0.01 |
| prove_TransferFromAllowanceReachesZero | PASS | 0.2 | 0.21 | 0.2 | 0.2 | 0.21 | 0.2 | 0.2 | 0.23 | 0.2 | 0.2| 0.21 | 0.01 |
| prove_TransferFromDecreasesAllowance | PASS | 0.15 | 0.15 | 0.14 | 0.14 | 0.15 | 0.14 | 0.15 | 0.15 | 0.25 | 0.14| 0.16 | 0.03 |
| prove_TransferFromDoesNotUpdateOtherBalances | PASS | 0.29 | 0.18 | 0.18 | 0.28 | 0.18 | 0.17 | 0.28 | 0.31 | 0.17 | 0.17| 0.22 | 0.06 |
| prove_TransferFromNoFees | PASS | 0.18 | 0.29 | 0.28 | 0.18 | 0.29 | 0.17 | 0.18 | 0.19 | 0.17 | 0.17| 0.21 | 0.05 |
| prove_TransferFromZeroAmount | PASS | 0.09 | 0.09 | 0.09 | 0.08 | 0.09 | 0.19 | 0.09 | 0.1 | 0.08 | 0.19| 0.11 | 0.04 |
| prove_TransferFromZeroAmountToZeroAddressReverts | ERROR | 0.05 | 0.05 | 0.06 | 0.05 | 0.06 | 0.05 | 0.06 | 0.06 | 0.05 | 0.05| 0.05 | 0.01 |
| prove_TransferZeroAmount | PASS | 0.07 | 0.07 | 0.07 | 0.07 | 0.08 | 0.07 | 0.07 | 0.07 | 0.07 | 0.07| 0.07 | 0.0 |
| prove_TransferZeroAmountToZeroAddressReverts | ERROR | 0.01 | 0.01 | 0.01 | 0.01 | 0.01 | 0.01 | 0.01 | 0.01 | 0.01 | 0.01| 0.01 | 0.0 |
| prove_ZeroAddressHasNoToken | PASS | 0.01 | 0.01 | 0.01 | 0.01 | 0.01 | 0.01 | 0.01 | 0.01 | 0.01 | 0.01| 0.01 | 0.0 |

**Total de Testes Feitos:** 65  

**Total de Testes Passados:** 53

**Total de Testes Com Erro do Halmos** 12

**Total de Testes que provam Vulnerabilidade** 0

# EM RELAÇÃO AO TEMPO TOTAL:

| TEMPO 1 | TEMPO 2 | TEMPO 3 | TEMPO 4 | TEMPO 5 | TEMPO 6 | TEMPO 7 | TEMPO 8 | TEMPO 9 | TEMPO 10 | Média  | Desvio Padrão |
|---------|---------|---------|---------|---------|---------|---------|---------|---------|----------|--------|----------------|
| 5,38    | 5,34    | 5,32    | 5,37    | 5,70    | 5,37    | 5,44    | 5,55    | 5,29    | 5,38     | 5,414  | 0,130          |


# OBSERVAÇÕES

**O tempo total de execução que o halmos entrega no output difere da soma do tempo de todos os testes(inconsistência)**  

**Nova versão do halmos com dificuldade de criar caminhos para provar os teoremas(alegam ser muito restritivos)**


# DESEMPENHO DO HALMOS NOS TESTES SIMBÓLICOS DO ERC721 (OPPEN ZEPPELIN)


| Função | Status | Tempo 1 | Tempo 2 | Tempo 3 | Tempo 4 | Tempo 5 | Tempo 6 | Tempo 7 | Tempo 8 | Tempo 9 | Tempo 10 | Média (s) | Desvio Padrão (s) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| proveFail_ApproveWhenIdHasNotAnOwner | PASS | 0.02 | 0.02 | 0.02 | 0.02 | 0.02 | 0.02 | 0.02 | 0.02 | 0.02 | 0.02 | 0.02 | 0.0 |
| proveFail_ApproveWhenIsNotApprovedForAll | PASS | 0.09 | 0.09 | 0.09 | 0.09 | 0.09 | 0.09 | 0.09 | 0.09 | 0.09 | 0.09 | 0.09 | 0.0 |
| proveFail_Burn | PASS | 0.01 | 0.01 | 0.01 | 0.01 | 0.01 | 0.01 | 0.01 | 0.01 | 0.01 | 0.01 | 0.01 | 0.0 |
| proveFail_MintWhenToIsAddressZero | PASS | 0.01 | 0.01 | 0.01 | 0.01 | 0.01 | 0.01 | 0.01 | 0.01 | 0.01 | 0.01 | 0.01 | 0.0 |
| proveFail_setApprovalForAll | PASS | 0.04 | 0.04 | 0.06 | 0.06 | 0.06 | 0.06 | 0.06 | 0.06 | 0.04 | 0.06 | 0.05 | 0.01 |
| proveFail_transferFromWhenFromIsNotTheOwner | PASS | 0.03 | 0.03 | 0.03 | 0.03 | 0.03 | 0.03 | 0.03 | 0.03 | 0.03 | 0.03 | 0.03 | 0.0 |
| proveFail_transferFromWhenToIsAddressZero | PASS | 0.07 | 0.08 | 0.07 | 0.07 | 0.07 | 0.07 | 0.07 | 0.07 | 0.07 | 0.07 | 0.07 | 0.0 |
| prove_ApproveWhenIsApprovedForAllOnwerDifferentFromMSGSender | PASS | 0.08 | 0.09 | 0.09 | 0.09 | 0.09 | 0.08 | 0.08 | 0.09 | 0.08 | 0.08 | 0.08 | 0.01 |
| prove_ApproveWhenOwnerEqualsMSGSender | PASS | 0.05 | 0.05 | 0.05 | 0.05 | 0.05 | 0.05 | 0.05 | 0.05 | 0.05 | 0.05 | 0.05 | 0.0 |
| prove_Burn | PASS | 0.06 | 0.07 | 0.07 | 0.07 | 0.07 | 0.07 | 0.07 | 0.07 | 0.06 | 0.06 | 0.07 | 0.0 |
| prove_Mint | PASS | 0.05 | 0.05 | 0.05 | 0.05 | 0.05 | 0.05 | 0.05 | 0.05 | 0.05 | 0.05 | 0.05 | 0.0 |
| prove_safeTransferFrom | FAIL | 0.12 | 0.12 | 0.13 | 0.13 | 0.12 | 0.12 | 0.12 | 0.12 | 0.12 | 0.12 | 0.12 | 0.0 |
| prove_setApprovalForAll | PASS | 0.03 | 0.03 | 0.03 | 0.03 | 0.03 | 0.03 | 0.03 | 0.03 | 0.03 | 0.03 | 0.03 | 0.0 |
| prove_transferFrom | PASS | 0.14 | 0.15 | 0.16 | 0.15 | 0.15 | 0.15 | 0.15 | 0.15 | 0.14 | 0.15 | 0.15 | 0.01 |

**Total de Testes Feitos:** 14 

**Total de Testes Passados:** 13

**Total de Testes Com Erro do Halmos** 0

**Total de Testes que provam Vulnerabilidade** 1

# EM RELAÇÃO AO TEMPO TOTAL:

| TEMPO 1 | TEMPO 2 | TEMPO 3 | TEMPO 4 | TEMPO 5 | TEMPO 6 | TEMPO 7 | TEMPO 8 | TEMPO 9 | TEMPO 10 | Média | Desvio Padrão |
|---------|---------|---------|---------|---------|---------|---------|---------|---------|----------|-------|----------------|
| 1,08    | 1,11    | 1,15    | 1,15    | 1,12    | 1,12    | 1,12    | 1,11    | 1,08    | 1,11     | 1,11  | 0,02           |

# OBSERVAÇÕES

**O tempo total de execução que o halmos entrega no output difere da soma do tempo de todos os testes(inconsistência)**  

**Nova versão do halmos executa os testes com excelência**  








# DESEMPENHO DO HALMOS NOS TESTES SIMBÓLICOS DO ERC1155 (OPPEN ZEPPELIN)  


| Função | Status | Tempo 1 | Tempo 2 | Tempo 3 | Tempo 4 | Tempo 5 | Tempo 6 | Tempo 7 | Tempo 8 | Tempo 9 | Tempo 10 | Média (s) | Desvio Padrão (s) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| proveFail_burnBalanceLessThanAmount | FAIL | 0.06 | 0.07 | 0.06 | 0.06 | 0.06 | 0.06 | 0.06 | 0.06 | 0.06 | 0.06 | 0.06 | 0.0 |
| proveFail_burnZeroAddress | PASS | 0.01 | 0.01 | 0.01 | 0.01 | 0.01 | 0.01 | 0.01 | 0.01 | 0.01 | 0.01 | 0.01 | 0.0 |
| proveFail_mintZeroAddress | PASS | 0.02 | 0.02 | 0.01 | 0.01 | 0.02 | 0.02 | 0.02 | 0.01 | 0.02 | 0.02 | 0.02 | 0.0 |
| proveFail_safeTransferFromBalanceLessThanAmount | FAIL | 0.05 | 0.05 | 0.05 | 0.05 | 0.05 | 0.05 | 0.05 | 0.05 | 0.05 | 0.05 | 0.05 | 0.0 |
| proveFail_safeTransferFromWhenSenderIsNotApprovedForAll | PASS | 0.06 | 0.07 | 0.06 | 0.06 | 0.07 | 0.06 | 0.07 | 0.06 | 0.07 | 0.06 | 0.06 | 0.01 |
| proveFail_safeTransferFromWhenSenderIsNotMSGSender | PASS | 0.02 | 0.02 | 0.02 | 0.02 | 0.02 | 0.02 | 0.02 | 0.02 | 0.02 | 0.02 | 0.02 | 0.0 |
| proveFail_safeTransferFromZeroAddressForFrom | PASS | 0.02 | 0.02 | 0.02 | 0.02 | 0.02 | 0.02 | 0.02 | 0.02 | 0.02 | 0.02 | 0.02 | 0.0 |
| proveFail_safeTransferFromZeroAddressForTo | PASS | 0.02 | 0.02 | 0.02 | 0.02 | 0.02 | 0.02 | 0.02 | 0.02 | 0.02 | 0.02 | 0.02 | 0.0 |
| proveFail_setApprovalForAllSenderEqualsOperator | PASS | 0.02 | 0.02 | 0.02 | 0.02 | 0.02 | 0.02 | 0.02 | 0.02 | 0.02 | 0.02 | 0.02 | 0.0 |
| prove_burn | FAIL | 0.04 | 0.04 | 0.04 | 0.04 | 0.04 | 0.04 | 0.04 | 0.04 | 0.04 | 0.04 | 0.04 | 0.0 |
| prove_mint | FAIL | 0.05 | 0.05 | 0.05 | 0.05 | 0.05 | 0.05 | 0.05 | 0.05 | 0.05 | 0.05 | 0.05 | 0.0 |
| prove_safeBatchTransferFrom | FAIL | 0.06 | 0.06 | 0.06 | 0.06 | 0.06 | 0.06 | 0.07 | 0.06 | 0.06 | 0.06 | 0.06 | 0.0 |
| prove_safeTransferFrom | FAIL | 0.04 | 0.04 | 0.04 | 0.04 | 0.04 | 0.04 | 0.05 | 0.04 | 0.04 | 0.04 | 0.04 | 0.0 |
| prove_setApprovalForAll | PASS | 0.03 | 0.04 | 0.03 | 0.03 | 0.03 | 0.04 | 0.04 | 0.03 | 0.03 | 0.03 | 0.03 | 0.0 |

**Total de Testes Feitos:** 14 

**Total de Testes Passados:** 8

**Total de Testes Com Erro do Halmos** 0

**Total de Testes que provam Vulnerabilidade** 6

# EM RELAÇÃO AO TEMPO TOTAL:

| TEMPO 1 | TEMPO 2 | TEMPO 3 | TEMPO 4 | TEMPO 5 | TEMPO 6 | TEMPO 7 | TEMPO 8 | TEMPO 9 | TEMPO 10 | Média | Desvio Padrão |
|---------|---------|---------|---------|---------|---------|---------|---------|---------|----------|-------|----------------|
| 0,74    | 0,81    | 0,75    | 0,74    | 0,76    | 0,78    | 0,83    | 0,75    | 0,80    | 0,75     | 0,77  | 0,03           |

# OBSERVAÇÕES

**O tempo total de execução que o halmos entrega no output difere da soma do tempo de todos os testes(inconsistência)**  

**Nova versão do halmos executa os testes com excelência**  



# DESEMPENHO DO HALMOS NOS TESTES SIMBÓLICOS DO ERC4626 (OPPEN ZEPPELIN)

# OBSERVAÇÕES

**Depois de realizado 20% dos testes, a demanda por memória ram dobra e o computador não aguentar rodar tudo.**  

**Por lidar com aritmética não linear, os testes demoram muito mais(nos anteriores, nenhum passou de 0.2s, nesse a maioria é entre 50s e 90s)** 

**Grande inconsistência nos tempos a cada run(os testes de arimética não linear variam muito de tempo de execução)** 





