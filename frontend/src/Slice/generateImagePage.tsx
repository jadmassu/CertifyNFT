import { createSlice, PayloadAction } from "@reduxjs/toolkit";
import { api } from "../utils/api";

export class Warranty {
    id: number = 0;
    name: string = "";
    shortName: string = "";
    description: string = "";
}
export class SearchParams {
    first = 0;
    rows = 7;
    searchText = "";
    sortColumn = "";
    sortDirection: number | null | undefined = 1;
}
interface ResStatus {
    status: number;
    msg: string;
}
interface State {
    warrantys: { count: number; rows: Warranty[] };
    warranty: Warranty;
    searchParams: SearchParams;
    resStatus: ResStatus;
    loading: boolean;
}

const initialState: State = {
    warrantys: { count: 0, rows: [] },
    warranty: {
        id: 0,
        name: "",
        shortName: "",
        description: "",
    },
    searchParams: {
        first: 0,
        rows: 7,
        searchText: "",
        sortColumn: "",
        sortDirection: 1,
    },
    resStatus: {
        status: -1,
        msg: "",
    },
    loading: false,
};
const WarrantySlice = createSlice({
    name: "warranty",
    initialState,
    reducers: {
        getWarrantys: (
            state: State,
            action: PayloadAction<{ count: number; rows: Warranty[] }>
        ) => {
            state.warrantys = action.payload;
        },
        addWarranty: (state: State, action: PayloadAction<Warranty>) => {
            state.warranty = action.payload;
        },
        setWarranty: (state: State, action: PayloadAction<Warranty>) => {
            state.warranty = action.payload;
        },
        addResStatus: (state: State, action: PayloadAction<ResStatus>) => {
            state.resStatus = action.payload;

        },
        setSearchParams: (state: State, action: PayloadAction<SearchParams>) => {
            state.searchParams = action.payload;
        },
        setLoading: (state: State, action: PayloadAction<boolean>) => {
            state.loading = action.payload;

        },
    },
});
export const {
    getWarrantys,
    addWarranty,
    setLoading,
    addResStatus,
    setSearchParams,
    setWarranty,
} = WarrantySlice.actions;
export default WarrantySlice.reducer;

const setResStatus = (resStatus: ResStatus) => async (dispatch: any) => {
    dispatch(addResStatus(resStatus));
    setTimeout(() => {
        dispatch(addResStatus({ status: -1, msg: "" }));
    }, 1000);
};

export const fetchWarrantys =
    (searchParams: SearchParams): any =>
        async (dispatch: any) => {
            try {
                dispatch(setLoading(true));
                const { first, rows, searchText, sortColumn, sortDirection } =
                    searchParams;
                const response = await api.get(
                    `/warrantys?f=${first}&r=${rows}&st=${searchText}&sc=${sortColumn}&sd=${sortDirection}&`,
                    config
                );
                let feedData = response.data;
                dispatch(getWarrantys(feedData));
                dispatch(setLoading(false));
            } catch (error: any) {
                dispatch(setLoading(false));
                dispatch(
                    setResStatus({
                        status: error.response.status,
                        msg: error.response.data.msg,
                    })
                );
            }
        };

export const createWarranty =
    (warranty: Warranty, searchParams: SearchParams): any =>
        async (dispatch: any) => {
            try {
                dispatch(setLoading(true));
                const response = await api.post("/warrantys", warranty, config);
                dispatch(
                    setResStatus({
                        status: response.status,
                        msg: "Warranty created successfully",
                    })
                );
                dispatch(fetchWarrantys(searchParams));
                dispatch(setLoading(false));
                dispatch(addWarranty(response.data));
            } catch (error: any) {
                dispatch(setLoading(false));
                dispatch(
                    setResStatus({
                        status: error.response.status,
                        msg: error.response.data.msg,
                    })
                );
            }
        };

export const updateWarranty =
    (warranty: Warranty, searchParams: SearchParams): any =>
        async (dispatch: any) => {
            try {
                dispatch(setLoading(true));
                const response = await api.put(
                    `/warrantys/${warranty.id}`,
                    warranty,
                    config
                );
                dispatch(fetchWarrantys(searchParams));
                dispatch(setLoading(false));
                dispatch(
                    setResStatus({
                        status: response.status,
                        msg: "Warranty updated sucessfuly",
                    })
                );
            } catch (error: any) {
                dispatch(setLoading(false));
                dispatch(
                    setResStatus({
                        status: error.response.status,
                        msg: error.response.data.msg,
                    })
                );
            }
        };

export const deleteWarranty =
    (warranty: Warranty): any =>
        async (dispatch: any) => {
            try {
                dispatch(setLoading(true));
                const response = await api.delete(`/warrantys/${warranty.id}`, config);
                dispatch(setLoading(false));
                dispatch(
                    setResStatus({
                        status: response.status,
                        msg: "Warranty deleted successfully",
                    })
                );
                dispatch(fetchWarrantys(new SearchParams()));
            } catch (error: any) {
                dispatch(setLoading(false));
                dispatch(
                    setResStatus({
                        status: error.response.status,
                        msg: error.response.data.msg,
                    })
                );
            }
        };
