from typing import Any, Dict, List, Mapping, Optional

from vital.api.api import API


class LabTests(API):
    """V3 endpoints for managing testkit orders."""

    def get_requisition_pdf(self, order_id: str) -> Any:
        """
        Gets the order requisition form in PDF format.
        """
        headers = {"Accept": "application/pdf"}
        return self.client.get(
            f"/order/{order_id}/requisition/pdf", api_version="v3", headers=headers
        )

    def register_testkit_order(
        self,
        user_id: str,
        sample_id: str,
        patient_details: dict,
        patient_address: dict,
        physician: Optional[dict] = None,
        consents: Optional[List[dict]] = None,
    ) -> Mapping[str, str]:
        """Register a testkit"""
        params = {
            "user_id": user_id,
            "sample_id": sample_id,
            "patient_details": patient_details,
            "patient_address": patient_address,
        }
        if physician:
            params["physician"] = physician
        if consents:
            params["consents"] = consents

        return self.client.post("/order/testkit/register", params, api_version="v3")

    def create_unregistered_testkit_order(
        self,
        user_id: str,
        lab_test_id: str,
        shipping_details: dict,
    ) -> Mapping[str, str]:
        """Order an unregistered testkit"""
        params = {
            "user_id": user_id,
            "lab_test_id": lab_test_id,
            "shipping_details": shipping_details,
        }

        return self.client.post("/order/testkit", params, api_version="v3")

    def create_order(
        self,
        user_id: str,
        patient_details: Dict,
        patient_address: Dict,
        lab_test_id: str,
        physician: Optional[Dict] = None,
        health_insurance: Optional[Dict] = None,
        priority: Optional[bool] = None,
        consents: Optional[List[dict]] = None,
    ) -> Mapping[str, str]:
        """Create new order"""
        params = {
            "user_id": user_id,
            "patient_details": patient_details,
            "patient_address": patient_address,
            "lab_test_id": lab_test_id,
            "physician": physician,
        }
        if health_insurance:
            params["health_insurance"] = health_insurance
        if priority:
            params["priority"] = priority
        if consents:
            params["consents"] = consents

        return self.client.post("/order", params, api_version="v3")

    def create_test(
        self,
        name: str,
        description: str,
        markers: List[str],
        lab_id: int,
        method: str,
        sample_type: str,
    ) -> Mapping[str, str]:
        """Create new lab test"""
        params = {
            "name": name,
            "description": description,
            "lab_id": lab_id,
            "method": method,
            "sample_type": sample_type,
            "marker_ids": markers,
        }

        return self.client.post("/lab_tests", params, api_version="v3")

    def get_orders(self, page: int = 1, size: int = 50) -> Mapping[str, str]:
        """Get all orders"""
        return self.client.get(
            "/orders",
            {"page": page, "size": size},
            api_version="v3",
        )

    def get_order(self, order_id: str) -> Mapping[str, str]:
        """
        Get order status.
        :param str user_id: The order_id.
        """
        return self.client.get(f"/order/{order_id}", api_version="v3")

    def cancel_order(self, order_id: str) -> Mapping[str, str]:
        """
        Cancel order.
        :param str user_id: The order_id.
        """
        return self.client.post(f"/order/{order_id}/cancel", api_version="v3")

    def search_payor(
        self, insurance_name: str, insurance_state: Optional[str] = None
    ) -> Mapping[str, str]:
        params = {"insurance_name": insurance_name}

        if insurance_state:
            params["insurance_state"] = insurance_state

        return self.client.post("/insurance/search/payor", params, api_version="v3")

    def search_diagnosis(self, diagnosis_query: str) -> Mapping[str, str]:
        return self.client.get(
            f"/insurance/search/diagnosis?diagnosis_query={diagnosis_query}",
            api_version="v3",
        )

    def get_tests(self) -> Mapping[str, str]:
        """
        GET all lab tests the team has access to.
        """
        return self.client.get("/lab_tests", api_version="v3")

    def get_results(self, order_id: str) -> Mapping[str, str]:
        """
        GET both metadata and raw json test data.
        """
        return self.client.get(f"/order/{order_id}/result", api_version="v3")

    def get_results_pdf(self, order_id: str) -> Mapping[str, str]:
        """
        GET gets the lab result for the order in PDF format.
        """
        return self.client.get(f"/order/{order_id}/result/pdf", api_version="v3")

    def get_results_metadata(self, order_id: str) -> Mapping[str, str]:
        """
        GET metadata related to order results, such as
        lab metadata, provider and sample dates.
        """
        return self.client.get(f"/order/{order_id}/result/metadata", api_version="v3")

    def get_area_info(self, zip_code: str) -> Mapping[str, str]:
        """
        GET area info for a given zip code.
        """
        return self.client.get("/area/info", {"zip_code": zip_code}, api_version="v3")
